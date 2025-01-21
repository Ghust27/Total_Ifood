# API Total gasto iFood

## Descrição
Esta API permite ao usuário obter um resumo dos gastos no iFood, incluindo o total gasto, métodos de pagamento utilizados e os principais restaurantes com base nas ordens concluídas. O projeto é baseado no Flask e interage com a API do iFood.

## Funcionalidades
- **Obter Total Gasto no iFood**: Recebe um token Bearer e retorna o total gasto, métodos de pagamento utilizados e os principais restaurantes por gasto e pedidos.

## Tecnologias Utilizadas
- Python
- Flask
- Flask-CORS
- Requests
- Dateutil

## Uso

1. Execute a aplicação:
   ```sh
   python app.py

2. Faça uma requisição POST para http://127.0.0.1:5000/get_total_ifood (o endereço pode variar de acordo com as mudanças do usuário) com o seguinte payload JSON:
```sh
{
  "token": "SEU_TOKEN_BEARER"
}
```

## Exemplo de Resposta:
```sh
{
  "total_spent": "1234.56",
  "currency": "BRL",
  "time_period": {
    "start_date": "01/01/2023",
    "end_date": "31/12/2023",
    "years": 0,
    "months": 11,
    "days": 30
  },
  "top_restaurants_by_spending": [
    {
      "name": "Restaurant A",
      "orders": 10,
      "total_spent": "456.78"
    },
    {
      "name": "Restaurant B",
      "orders": 5,
      "total_spent": "234.56"
    },
    {
      "name": "Restaurant C",
      "orders": 3,
      "total_spent": "123.45"
    }
  ],
  "top_restaurants_by_orders": [
    {
      "name": "Restaurant A",
      "orders": 10,
      "total_spent": "456.78"
    },
    {
      "name": "Restaurant B",
      "orders": 5,
      "total_spent": "234.56"
    },
    {
      "name": "Restaurant C",
      "orders": 3,
      "total_spent": "123.45"
    }
  ],
  "payment_methods": {
    "Credit": 1000,
    "Debit": 234.56
  }
}
```
---

# Total spent iFood API

## Description
This API allows users to obtain a summary of their spending on iFood, including total expenditure, payment methods used, and top restaurants based on completed orders. The project is built with Flask and interacts with the iFood API.

## Features
- **Get Total Spent on iFood**: Receives a Bearer token and returns the total spent, payment methods used, and top restaurants by spending and orders.

## Technologies Used
- Python
- Flask
- Flask-CORS
- Requests
- Dateutil

## Usage

1. Run the application:
   ```sh
   python app.py

Make a POST request to http://127.0.0.1:5000/get_total_ifood (the address may vary based on user changes) with the following JSON payload:
```sh
{
  "token": "YOUR_BEARER_TOKEN"
}
```

## Response Example:

```sh
{
  "total_spent": "1234.56",
  "currency": "BRL",
  "time_period": {
    "start_date": "01/01/2023",
    "end_date": "31/12/2023",
    "years": 0,
    "months": 11,
    "days": 30
  },
  "top_restaurants_by_spending": [
    {
      "name": "Restaurant A",
      "orders": 10,
      "total_spent": "456.78"
    },
    {
      "name": "Restaurant B",
      "orders": 5,
      "total_spent": "234.56"
    },
    {
      "name": "Restaurant C",
      "orders": 3,
      "total_spent": "123.45"
    }
  ],
  "top_restaurants_by_orders": [
    {
      "name": "Restaurant A",
      "orders": 10,
      "total_spent": "456.78"
    },
    {
      "name": "Restaurant B",
      "orders": 5,
      "total_spent": "234.56"
    },
    {
      "name": "Restaurant C",
      "orders": 3,
      "total_spent": "123.45"
    }
  ],
  "payment_methods": {
    "Credit": 1000,
    "Debit": 234.56
  }
}

```
---
