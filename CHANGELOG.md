# WIP


# Version 0.1: start of assignment

## Changes:

src/unc/__init__.py

* line 3
 import math
 import sys
 from typing import Any
-------------------------------------------------------------------------------
 * line 6
 -
 if sys.version_info < (3, 11):
     from typing_extensions import Self

-------------------------------------------------------------------------------
 * line 48
    def __add__(self: Self, other: LabUnc) -> Self:
        return self.__class__(self.n + other.n, self.combine(self.s, other.s))

 * line 51
    def __sub__(self: Self, other: LabUnc) -> Self:
        return self.__class__(self.n - other.n, self.combine(self.s, other.s))

 * line 54
    def __mul__(self: Self, other: LabUnc) -> Self:
        C = self.n * other.n

 * line 59
    def __truediv__(self: Self, other: LabUnc) -> Self:
         C = self.n / other.n
