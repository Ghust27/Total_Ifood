import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Data:
    def __init__(self):
        self.headers = {
            "authorization": ""
        }
        self.datas = []
        self.time = {"inicio": "", "final": ""}
        self.base_url = "https://marketplace.ifood.com.br/v4/customers/me/orders"

    def getJsonData(self):
        print("Coletando Dados...")
        try:
            i = 0
            while True:
                resp = requests.get(f'{self.base_url}?page={i}&size=25', headers=self.headers, verify=False)
                if resp.status_code != 200:
                    return {"Error":"Wrong Bearer Token."},resp.status_code  
                page_data = resp.json()  
                self.datas.extend(page_data)
                if len(page_data) < 25:
                    break
                i += 1
            print("Dados coletados!")
            return 200
        except Exception as e:
            return {"Error": str(e)}, resp.status_code

    def getTotalSpent(self):
        if not self.datas:
            return {"error": "No data"}, 404

        payments_methods = {}
        restaurantes = {}
        coin = self.datas[0]["payments"]["total"]["currency"]

        for i, order in enumerate(self.datas):
            if order["lastStatus"] == "CONCLUDED":
                method_name = order["payments"]["methods"][0]["method"]["name"]
                payment_value = round(order["payments"]["total"]["value"] / 100, 2)
                restaurante = order["merchant"]["name"]

                if restaurante not in restaurantes:
                    restaurantes[restaurante] = {"total_gasto": payment_value, "quantidade_pedidos": 1}
                else:
                    restaurantes[restaurante]["total_gasto"] += payment_value
                    restaurantes[restaurante]["quantidade_pedidos"] += 1

                if i == 0:
                    self.time["final"] = order["createdAt"].split("T")[0]
                if i == len(self.datas) - 1:
                    self.time["inicio"] = order["createdAt"].split("T")[0]

                if method_name not in payments_methods:
                    payments_methods[method_name] = payment_value 
                else:
                    payments_methods[method_name] = round(payments_methods[method_name] + payment_value, 2)

        total_spent = round(sum(payments_methods.values()), 2)

        top_restaurantes_por_gasto = sorted(restaurantes.items(), key=lambda item: item[1]["total_gasto"], reverse=True)[:3]
        top_restaurantes_por_pedidos = sorted(restaurantes.items(), key=lambda item: item[1]["quantidade_pedidos"], reverse=True)[:3]

        inicio_formato_br = datetime.strptime(self.time["inicio"], "%Y-%m-%d").strftime("%d/%m/%Y")
        final_formato_br = datetime.strptime(self.time["final"], "%Y-%m-%d").strftime("%d/%m/%Y")

        data_inicio = datetime.strptime(self.time["inicio"], "%Y-%m-%d")
        data_final = datetime.strptime(self.time["final"], "%Y-%m-%d")
        diferenca = relativedelta(data_final, data_inicio)
        meses = diferenca.months
        dias = diferenca.days
        anos = diferenca.years

        result = {
            "total_spent": f"{total_spent:.2f}",
            "currency": coin,
            "time_period": {
                "start_date": inicio_formato_br,
                "end_date": final_formato_br,
                "years": anos,
                "months": meses,
                "days": dias
            },
            "top_restaurants_by_spending": [
                {"name": nome, "orders": dados["quantidade_pedidos"], "total_spent": f"{dados['total_gasto']:.2f}"}
                for nome, dados in top_restaurantes_por_gasto
            ],
            "top_restaurants_by_orders": [
                {"name": nome, "orders": dados["quantidade_pedidos"], "total_spent": f"{dados['total_gasto']:.2f}"}
                for nome, dados in top_restaurantes_por_pedidos
            ],
            "payment_methods": payments_methods
        }
        
        return result, 200
    
    def get_total_ifood(self):
        status = self.getJsonData()
        if status != 200:
            return status
        return self.getTotalSpent()
