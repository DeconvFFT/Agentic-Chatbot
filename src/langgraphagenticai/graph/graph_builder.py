from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot import BasicChatbotNode
from src.langgraphagenticai.tools.tools import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.nodes.chatbot_with_tools import ChatbotwithTools

## This workflow will get triggered once we have user inputs from UI and
## our LLM is loaded
class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langgraph.
        The method initializes a chatbot node using `BasicChatbotNode` class
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph
        """
        
        ## basic chatbot node
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        ## Build graph
        self.graph_builder.add_node('chatbot', self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)
    
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initialises chatbot with the tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as entry point
        """
        ## get tools
        tools = get_tools()
        tool_node = create_tool_node(tools)
        
        ## define LLM
        llm = self.llm
        
        ## Define chatbot node
        obj_chatbot_with_tools = ChatbotwithTools(llm)
        self.chatbot_with_tools_node = obj_chatbot_with_tools.create_chatbot(tools)
        ## add nodes
        self.graph_builder.add_node('chatbot', self.chatbot_with_tools_node)
        self.graph_builder.add_node('tools', tool_node)
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_conditional_edges(
            'chatbot',
            tools_condition
        )
        self.graph_builder.add_edge('tools', 'chatbot')
        
        
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == 'Chatbot With Tools':
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()