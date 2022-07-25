import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class ContextDTO:
    id: str = ""
    context: str = ""
    lifespan: int = 0
    text: str = ""
    finish: str = ""
