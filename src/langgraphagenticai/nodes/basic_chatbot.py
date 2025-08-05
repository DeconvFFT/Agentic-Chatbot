from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """ 
    Basic chatbot node
    """
    def __init__(self, model):
        self.llm = model
        
    def process(self, state:State) -> dict:
        """
        Process the input state and generates a chatbot response

        Args:
            state (dict): The input state

        Returns:
            dict: Updated state
        """
        return {'messages': self.llm.invoke({state['messages']})}
    