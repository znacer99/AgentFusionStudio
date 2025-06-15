# main.py (updated without dotenv)
import os
from fastapi import FastAPI
from agent import SocialMediaAgent

app = FastAPI()
agent = SocialMediaAgent()

# Manual environment loading (no dotenv needed)
def load_env():
    env_vars = {}
    try:
        with open('.env') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
    except FileNotFoundError:
        pass
    return env_vars

env = load_env()

@app.get("/")
def read_root():
    return {
        "message": "Social Agent Studio is running!",
        "agent": agent.name,
        "description": agent.description
    }

@app.post("/publish")
def publish_content(platform: str, content: str):
    result = agent.publish(platform, content)
    return {"status": "success", "result": result}