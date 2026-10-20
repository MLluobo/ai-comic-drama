from server.states import ComicDramaState

def receive_idea(state:ComicDramaState) -> ComicDramaState:
    """接收用户最初的输入"""
    raw_requirement = state["raw_requirement"].strip()

    if not raw_requirement:
        raise ValueError("raw_requirement 不能为空，请先输入漫剧创意")
    
    return {
        "raw_requirement":raw_requirement,
        "current_stage": "idea_received",
        "events": ["已接收用户创意"],
    }