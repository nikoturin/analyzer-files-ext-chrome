from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain.prompts import(
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import PyPDFLoader

class llmPoliceInfo():

    def __init__(self,action):
        self.input=action

    def test(self):
        print(f"{self.input}")

    def analyzeFile(self,pages):

        user_input= """
                Analiza la información y responde si encuentras palabras clave como: 
                "usuarios"
                "password"
                "rfc"
                "curp" 
                "dirección"
                "teléfonos"
                "nombre empleados"
                Encontrada alguna palabra clave como las anteriores, responde con una advertencia.
        """
        system_template= """
            #Role:
                    Eres un experto analista de grandes volumenes información, con especialidad en ciberseguridad, tomando que utilizas muchas técnicas
                    para el análisis extenso de información de cualquier índole.
            #Objetivo:
                    La tarea que tienes es la de análizar información correspondiente a la organización, donde deberás analizar que archivos con extensión
                    .pdf, .txt, .csv u otro tipo de formato, no contengan usuarios y password, así como información personal tal como dirección, rfc, curp.
            #Contexto:
                    En la actualidad el simple hecho de exponer información personal, podríamos ser sancionados por leyes como GDPR o a través de la protección de datos personales de México.
            #Ejemplo:
                    "input": Requiero que busques información sensible tal como usuarios y password
                    "Respuesta": Se encontró información de usuarios y password, será importante que revise el archivo que será analizado.
                    "input": Requiero busques información personal de empleados.
                    "Respuesta": Se ha encontrado información personal de algunos empleados, será importante que revise información que está subiendo.

        """
        system_prompt=SystemMessagePromptTemplate.from_template(system_template)

        contenido_pdf=pages[0].page_content

        human_template='"{input}: \n{contenido}"'
        human_prompt=HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt=ChatPromptTemplate.from_messages([system_prompt,human_prompt])
        chat_prompt.format_prompt(input=user_input,contenido=contenido_pdf)

        documento_completo=""
        for page in pages:
            documento_completo+=page.page_content

        solicitud_completa=chat_prompt.format_prompt(input=user_input,contenido=documento_completo).to_messages()

        chat=ChatOllama(model="gemma:2b",temperature=0,base_url="http://<ip model server>:11434")
        result = chat.invoke(solicitud_completa)

        return result.content
