from typing import Any, ClassVar

from ..rdBase import _vectj

class AtomPairsParameters:
    atomTypes: ClassVar[_vectj]
    codeSize: ClassVar[int]
    numAtomPairFingerprintBits: ClassVar[int]
    numBranchBits: ClassVar[int]
    numChiralBits: ClassVar[int]
    numPathBits: ClassVar[int]
    numPiBits: ClassVar[int]
    numTypeBits: ClassVar[int]
    version: ClassVar[str]
