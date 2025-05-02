# analyzer-files-ext-chrome
This project was created to protect the information some people try to get out, I mean, every three month cibersecurity area make some compains to share information about the cibersecurity risk, including the best way to use IA, in this case public IA.

By this reason I decided to build extension chrome to make a double check at files trying to process using IA public, in this case I used Private IA we installed at company, in this case using **gemma 2b model.**

Note: at the moment, all test I did were using gemini public model, I hope to do some test with chatgpt soon.

In this case you try to use gemini or chatgpt public model, and before to execute any submit, the information is sent to internal or private IA to be processed, analizing information you trying to upload, and if the information found some information about "credentails" or sensible information about the company, this launch a popup to sharing information about the results analyze.

![Image](https://github.com/user-attachments/assets/a063ee32-083a-4669-97e4-033743f48b11)

# Steps workflow 

1.- at the moment is open, but just to evaluate chatgpt or gemmini webpage will necesary to configure "manifest.json" file.

2.- The user upload the file, in this case content.js detect the event "change", across tagName "INPUT",

3.- Content.js send message to background.js(service-worker), message with bytes of file ...

4.- service-worker send data to api with object name=items/

5.- api built a file, in this case "txt", it was to start proof, but a couple of day I'll change to pdf or csv etc...

6.- using langchain read data from file "txt", using the tools; 

7.- Invoke internal model, in this case gemma 2b(small model) installed at on-prem infraestucture

    Note: I've downloaded short model, because on-prem not guarantie power of model, I mean, procesed information with CPU, I'll test it at aws using gpu.
    
8.- with instrucctions Prompt has, detect some case about sensible information of company, is important to keep in mind what information is sensible for your company.

9.- At the moment the output of API popup a message "alert message", just to check the result of analyze.

By this reason, it was initial project, I'll start work other cases and I'll add the MCP protocol.

# Steps I've worked internal:

-  I've changed the manifest
-  
-  When the information found any sensible information, you cannot upload the file.
-  
-  And send email to some peoples on charge security.

