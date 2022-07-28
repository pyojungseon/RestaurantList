import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class RequestDTO:
    userId: str = ""
    content: str = ""
    header: str = ""
    tag: str = ""
    lifeSpan: int = 0
    param1: str = ""
    param2: str = ""
    param3: str = ""
    param4: str = ""
    param5: str = ""

