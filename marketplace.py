from fastapi import FastAPI
from agent import Agent
from marketplace import Marketplace

app = FastAPI()
market = Marketplace()

#Add sample agent at startup
@app.on_event("startup")
def startup_event():
    market.add_agent(Agent("Text Uppercaser", "Makes Text uppercase"))
    
@app.get("/agents")
def list_agents():
    return [{"id": agent.id, "name": vipo} for agent in market.agent.values]
