import json
from llm import llmPoliceInfo
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from fastapi import FastAPI, UploadFile,File
from pathlib import Path
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

UPLOAD_DIR= Path()/'files'
app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
    analizeStr=llmPoliceInfo("Activate") 
    tmp_pdf = "./tmp.txt"
    with open(tmp_pdf,'w') as pdfFile:
        pdfFile.write(item.description)
        
    loader=TextLoader(tmp_pdf)
    pages=loader.load_and_split()
    
    response=analizeStr.analyzeFile(pages)

    print(f"{type(item.description)} response PoliceInfo: {response}")
    return response
