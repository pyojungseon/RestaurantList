import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class restaurantDTO:
    seq: int = 0
    name: str = ""
    tag: str = ""
    lprice: int = 0
    hprice: int = 0
    map: str = ""
    moksung: str = "N"
    payco: str = "N"
    mn5: str = "N"
    mn4: str = "N"
    mn2: str = "N"
    eval: str = ""
