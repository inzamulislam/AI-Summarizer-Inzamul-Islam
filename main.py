from fastapi import FastAPI
import requests
app = FastAPI()
@app.post("/submit")
def handle_request(data: dict):
    n8n_url = "http://localhost:5678/webhook-test/submit"
    requests.post(n8n_url, json=data)
    return {"message": "Success"}