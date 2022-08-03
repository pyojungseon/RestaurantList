import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class sugDTO:
    id : str = ""
    content : str = ""
