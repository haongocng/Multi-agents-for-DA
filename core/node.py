from langchain_core.messages import AIMessage, HumanMessage
from core.state import State
import logging
from langchain.agents import AgentExecutor

logger = logging.getLogger(__name__)

def agent_node(state: State, agent: AgentExecutor, name: str) -> dict:
    """
    Invokes the agent, updates the state with the agent's output, and
    trims the message history to prevent it from getting too long.
    """
    logger.info(f"--- Executing agent: {name} ---")
    try:
        # You can adjust the number of messages to pass, e.g., state["messages"][-6:]
        state_for_agent = state.copy()
        state_for_agent["messages"] = state["messages"][-6:]

        result = agent.invoke(state_for_agent)
        
        output = result.get("output", "")
        
        ai_message = AIMessage(content=output, name=name)
        
        state["messages"].append(ai_message)
        state["sender"] = name
        
        if name == "DataExplorer":
            state["eda_report"] = output
            logger.info("State updated with EDA Report.")
        elif name == "DataStatistic":
            state["statistic_report"] = output
            logger.info("State updated with Statistic Report.")
        elif name == "DataCluster":
            state["cluster_report"] = output
            logger.info("State updated with Cluster Report.")
        elif name == "DataVisualization":
            state["visualization_report"] = output
            logger.info("State updated with Visualization Report.")
        elif name == "HypothesisGenerator":
            state["hypothesis_report"] = output
            logger.info("State updated with Hypothesis Report.")
        elif name == "Reasoner":
            state["reasoning_report"] = output
            logger.info("State updated with Reasoning Report.")
        elif name == "QualityReview":
            state["total_summary_report"] = output
            logger.info("State updated with Total Summary Report.")
        elif name == "Synthesis":
            state["final_report"] = output
            logger.info("State updated with Final Insights Report.")
            
        logger.info(f"--- Finished agent: {name} ---")
        return state

    except Exception as e:
        logger.error(f"Error occurred while processing agent {name}: {str(e)}", exc_info=True)
        error_message = AIMessage(content=f"Error in agent {name}: {str(e)}", name="error")
        state["messages"].append(error_message)
        return state

logger.info("Agent processing node module initialized")