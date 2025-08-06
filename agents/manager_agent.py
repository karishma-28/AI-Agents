from agents import agent1, agent2, agent3

def decide_and_execute(user_input: str, documents_path: str = None) -> dict:
    selected_agents = []
    responses = {}

    if "summarize" in user_input or "keywords" in user_input:
        selected_agents.append("Agent1")
        responses["Agent1"] = {
            "status": 200,
            "data": agent1.summarize_and_extract_keywords(user_input)
        }

    if "query" in user_input and documents_path:
        selected_agents.append("Agent2")
        responses["Agent2"] = {
            "status": 200,
            "data": agent2.respond_to_query(documents_path, user_input)
        }

    if "current" in user_input or "latest" in user_input:
        selected_agents.append("Agent3")
        responses["Agent3"] = {
            "status": 200,
            "data": agent3.fetch_from_internet(user_input)
        }

    return {
        "manager_agent": {
            "decision": f"Selected based on input analysis: {user_input}",
            "selected_agents": selected_agents
        },
        "agent_responses": responses
    }
