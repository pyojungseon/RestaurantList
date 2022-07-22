import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class LogDTO:
    id : str = ""
    content : str = ""
    tag : str = ""