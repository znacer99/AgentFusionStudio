from fastapi import FastAPI
from agent import Agent
from marketplace import Marketplace  # This import is OK here

app = FastAPI()
market = Marketplace()

@app.on_event("startup")
def startup_event():
    market.add_agent(Agent("Text Uppercaser", "Makes text uppercase"))

@app.get("/agents")
def list_agents():
    return [{"id": agent.id, "name": agent.name} for agent in market.agents.values()]