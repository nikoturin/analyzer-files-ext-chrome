// content_script.js

console.log("Content Script to analize internaly txt files ...");

document.addEventListener('change', (event) => {
  // Actions just on inputs type txt-plain
  if (event.target.tagName === 'INPUT' && event.target.type === 'file') {
    const files = event.target.files;

    if (files.length > 0) {
      for (const file of files) {
        const isTxt = file.type === 'text/plain';

        if (isTxt) {
          console.log(`TXT detectado: ${file.name} (${file.size} bytes)`);

          const reader = new FileReader();

          reader.onload = (e) => {
            const pdfBuffer = e.target.result;
            console.log(`PDF leído como ArrayBuffer (tamaño: ${pdfBuffer.byteLength}).`);

            console.log(`Sending TXT File to Analize '${pdfBuffer.name}' and background script...`);
            chrome.runtime.sendMessage({
              type: "UPLOAD_TXT",
              fileName: file.name,
              fileType: file.type,
              fileBuffer: pdfBuffer
            }).then(response => {
                 console.log("Answer of background script (upload):", response);
                 alert(response.data)
            }).catch(error => {
                if (error.message.includes("Receiving end does not exist")) {
                    console.warn("Background script is not active and does not have listener to upload TXT");
                } else {
                    console.error("Error Sending msg UPLOAD_TXT to background script:", error);
                }
            });
          };

          reader.onerror = (e) => {
            console.error(`Error Reading TXT File ... '${file.name}':`, e);
          };

          //reader.readAsArrayBuffer(file); // Should be this way, but ok I'll check my next versión ...
          reader.readAsText(file)

        } else {
          console.log(`File '${file.name}' ignore (is not a TXT File).`);
        }
      }
    }
  }
}, false);