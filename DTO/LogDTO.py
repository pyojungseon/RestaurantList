import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class LogDTO:
    def __init__(self):
        pass

    id : str = ""
    content : str = ""
    tag : str = ""
