# marketplace.py - CORRECTED VERSION
class Marketplace:
    def __init__(self):
        self.agents = {}
        
    def add_agent(self, agent):
        self.agents[agent.id] = agent
        
    def get_agent(self, agent_id):
        return self.agents.get(agent_id)