# agent.py
class SocialMediaAgent:
    def __init__(self):
        self.name = "Social Media Publisher"
        self.description = "Publishes content to social platforms"
        
    def publish(self, platform, content):
        """Simulate publishing - we'll add real APIs later"""
        return f"Posted to {platform}: {content}"