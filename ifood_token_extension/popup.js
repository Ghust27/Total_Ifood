document.getElementById('getToken').addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: 'getToken' }, (response) => {
    const tokenTextarea = document.getElementById('token');
    const copyButton = document.getElementById('copyToken');
    const notification = document.getElementById('notification');
    const loginNotification = document.getElementById('loginNotification');

    if (response.token) {
      tokenTextarea.value = response.token;
      copyButton.disabled = false;
      loginNotification.style.display = 'none';
    } else {
      tokenTextarea.value = '';
      copyButton.disabled = true;
      loginNotification.style.display = 'block';
      setTimeout(() => {
        loginNotification.style.display = 'none';
      }, 5000);
    }
  });
});

document.getElementById('copyToken').addEventListener('click', () => {
  const tokenTextarea = document.getElementById('token');
  tokenTextarea.select();
  document.execCommand('copy');
  
  const notification = document.getElementById('notification');
  notification.style.display = 'block';
  setTimeout(() => {
    notification.style.display = 'none';
  }, 3000);
});
