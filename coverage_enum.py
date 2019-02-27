from enum import Enum


class CoverageType(Enum):
    NONE = 0,
    CLASS = 1,
    METHOD = 2,
    BLOCK = 3,
    LINE = 4
