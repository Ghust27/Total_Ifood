let bearerToken = '';

chrome.webRequest.onBeforeSendHeaders.addListener(
  (details) => {
    for (let header of details.requestHeaders) {
      if (header.name.toLowerCase() === 'authorization' && header.value.startsWith('Bearer ')) {
        bearerToken = header.value.replace('Bearer ', ''); // Remover o prefixo "Bearer "
        break;
      }
    }
    return { requestHeaders: details.requestHeaders };
  },
  { urls: ["<all_urls>"] },
  ["requestHeaders"]
);

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'getToken') {
    sendResponse({ token: bearerToken });
  }
});
