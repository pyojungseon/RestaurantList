import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class ContextDTO:
    id: str = ""
    tag: str = ""
    lifespan: int = 0
    text: str = ""
    finish: str = ""
