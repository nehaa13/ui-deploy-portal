from fastapi import FastAPI
from config_reader import *
from github_trigger import trigger_workflow

app = FastAPI()

@app.get("/lobs")
def get_lobs():
    return list_lobs()

@app.get("/envs")
def get_envs(lob: str):
    return list_envs(lob)

@app.get("/packages")
def get_packages(lob: str, env: str):
    return list_packages(lob, env)

@app.get("/servers")
def get_servers(lob: str, env: str):
    return list_servers(lob, env)

@app.post("/deploy")
def deploy(payload: dict):
    trigger_workflow(payload)
    return {"status": "triggered"}
