import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class RequestDTO:
    userId: str = ""
    content: str = ""
    header: str = ""
    tag: str = ""
    lifeSpan: int = 0
