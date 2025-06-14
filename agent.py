class Agent:
    def __init__(self, name, description):
        self.id = f"agent_{id(self)}"
        self.name = name
        self.description = description
    
    def execute(self, input_data):
        return f"{self.name} processed: {input_data}"