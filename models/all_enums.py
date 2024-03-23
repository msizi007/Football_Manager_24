from enum import Enum, auto


class Position(Enum):
    GK = auto()
    LCB = auto()
    RCB = auto()
    LB = auto()
    RB = auto()
    LDM = auto()
    RDM = auto()
    LCM = auto()
    RCM = auto()
    CM = auto()
    LAM = auto()
    RAM = auto()
    LM = auto()
    RM = auto()
    LW = auto()
    RW = auto()
    CST = auto()
    LST = auto()
    ST = auto()

# ALL FORMATIONS
class Formation(Enum):
    F442 = {"positions": [Position.GK, Position.LCB, Position.RCB,
        Position.LB, Position.RB, Position.LCM, Position.RCM,
        Position.LM, Position.RM, Position.LST, Position.RST]}
    F443 = {"positions": [Position.GK, Position.LCB, Position.RCB,
        Position.LB, Position.RB, Position.LCM, Position.RCM, Position.CM,
        Position.RW, Position.LW, Position.ST]}

class Nation(Enum):
    France = auto()
    Italy = auto()
    Spain = auto()
    Germany = auto()
    Russia = auto()
    Poland = auto()
    Portugal = auto()
    Brazil = auto()
    Argentina = auto()
    Australia = auto()
    Austria = auto()
    Sweden = auto()
    Switzerland = auto()
    Denmark = auto()
    Norway = auto()
    

class PlayerRole(Enum):
    Important = auto()
    Regular = auto()
    SquadPlayer = auto()
    SuperSub = auto()
    Sub = auto()
    BackUp = auto()
    Development = auto()

class PlayerAttributes(Enum):
    Technical = auto()
    Mental = auto()
    Physical = auto()
    