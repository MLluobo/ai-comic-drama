import operator
from typing import Annotated, TypedDict

class ComicDramaState(TypedDict):
    """整张图"""

    # 用户最初的输入
    # eg: 深夜的办公室里，程序员小林正在修改一款漫画应用。零点到来时，他设计的漫画角色阿沐突然从屏幕中走了出来。
    raw_requirement:str

    # 当前所处阶段
    current_stage:str

    events: Annotated[list[str], operator.add]
