// background.js

console.log("Service Worker - TXT Uploader Started ...");

const TXT_UPLOAD_API_URL = 'http://<ip api server>:8000/items';

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "UPLOAD_TXT") {
    console.log(`Receive TXT to upload: ${message.fileName} (${message.fileBuffer} bytes)`);

    if (!TXT_UPLOAD_API_URL) {
        console.error("¡Error! the URL of API is not configured at background.js.");
        sendResponse({ status: "Error", message: "URL of API is not configured." });
        return true;
    }

    const data = {name:"Sending TXT to analize",description:message.fileBuffer}

    fetch(TXT_UPLOAD_API_URL, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
    })
    .then( async response => {
      console.log('First Answer of Server (UPLOAD TXT):', response.status, response.statusText,response.ok);
      if (!response.ok) {
        const text = await response.text();
        throw new Error(`Server Error (UPLOAD TXT): ${response.status} ${response.statusText} - ${text}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Upload TXT File Correct ...', data);
      sendResponse({ status: "Éxito", data: data });
    })
    .catch(error => {
      console.error('Error during upload TXT File ... please do a double check:', error);
      sendResponse({ status: "Error", message: error.message || "Error unkown" });
    });

    return true;
  }
});   

console.log("Listener de chrome.runtime.onMessage añadido.");
