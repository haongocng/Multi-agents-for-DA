from langgraph.graph import StateGraph, END, START
from core.state import State
from core.node import agent_node 
from agents.explorer_agent import create_data_explorer_agent
from agents.statistic_agent import create_data_statistic_agent
from agents.cluster_agent import create_data_cluster_agent
from agents.visualization_agent import create_visualization_agent
from agents.hypothesis_agent import create_hypothesis_generator_agent
from agents.reasoner_agent import create_reasoner_agent
from agents.review_agent import create_quality_review_agent
from agents.synthesis_agent import create_synthesis_agent

class WorkflowManager:
    def __init__(self, language_models, working_directory):
        self.language_models = language_models
        self.working_directory = working_directory
        self.members = [
            "DataExplorer", "DataStatistic", "DataCluster", "DataVisualization",
            "HypothesisGenerator", "Reasoner", "QualityReview", "Synthesis"
        ]
        self.agents = self.create_agents()
        self.workflow = self.setup_workflow()

    def create_agents(self):
        """Create all system agents for the workflow"""
        llm = self.language_models["llm"]
        power_llm = self.language_models["power_llm"]
        
        agents = {
            "explorer": create_data_explorer_agent(llm, self.members, self.working_directory),
            "statistic": create_data_statistic_agent(llm, self.members, self.working_directory),
            "cluster": create_data_cluster_agent(llm, self.members, self.working_directory),
            "visualizer": create_visualization_agent(llm, self.members, self.working_directory),
            "hypothesis": create_hypothesis_generator_agent(llm, self.members, self.working_directory),
            "reasoner": create_reasoner_agent(power_llm, self.members, self.working_directory),
            "quality": create_quality_review_agent(power_llm, self.members, self.working_directory),
            "synthesis": create_synthesis_agent(power_llm, self.members, self.working_directory),
        }
        return agents

    def setup_workflow(self):
        """Set up the workflow graph"""
        graph = StateGraph(State)

        graph.add_node("DataExplorer", lambda state: agent_node(state, self.agents["explorer"], "DataExplorer"))
        graph.add_node("DataStatistic", lambda state: agent_node(state, self.agents["statistic"], "DataStatistic"))
        graph.add_node("DataCluster", lambda state: agent_node(state, self.agents["cluster"], "DataCluster"))
        graph.add_node("DataVisualization", lambda state: agent_node(state, self.agents["visualizer"], "DataVisualization"))
        graph.add_node("HypothesisGenerator", lambda state: agent_node(state, self.agents["hypothesis"], "HypothesisGenerator"))
        graph.add_node("Reasoner", lambda state: agent_node(state, self.agents["reasoner"], "Reasoner"))
        graph.add_node("QualityReview", lambda state: agent_node(state, self.agents["quality"], "QualityReview"))
        graph.add_node("Synthesis", lambda state: agent_node(state, self.agents["synthesis"], "Synthesis"))

        # Define the work flow the graph
        graph.add_edge(START, "DataExplorer")
        graph.add_edge("DataExplorer", "DataStatistic")
        graph.add_edge("DataStatistic", "DataCluster")
        graph.add_edge("DataCluster", "DataVisualization")
        graph.add_edge("DataVisualization", "HypothesisGenerator")
        graph.add_edge("HypothesisGenerator", "Reasoner")
        graph.add_edge("Reasoner", "QualityReview")
        graph.add_edge("QualityReview", "Synthesis")
        graph.add_edge("Synthesis", END)
        
        return graph.compile()

    def get_graph(self):
        return self.workflow