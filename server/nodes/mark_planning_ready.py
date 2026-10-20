from server.states import ComicDramaState

def mark_planning_ready(state:ComicDramaState) -> ComicDramaState:
    """标记为需求整理准备阶段"""
    if state["current_stage"] != "idea_received":
        raise ValueError("只有已接收的创意才能进入需求整理阶段")
    
    return {
        "current_stage": "planning_ready",
        "events": ["已进入需求整理准备阶段，开始整理需求"],
    }