from enum import Enum


class Figure(Enum):
    def __new__(cls, number, name):
        obj = bytes.__new__()
    ROI = "",
    DAME = "",
    VALET = "",
    NONE = ""
