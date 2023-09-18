from _typeshed import Incomplete
from . import Mol, Conformer, AtomPairsParameters
from ..Geometry import Point3D

def CanonicalizeConformer(conf: Conformer, center: None | Point3D = ..., normalizeCovar: bool = ..., ignoreHs: bool = True) -> None: ...
def CanonicalizeMol(mol: Mol, normalizeCovar: bool = ..., ignoreHs: bool = ...) -> None: ...
def ComputeCanonicalTransform(conf: Conformer, center: None | Point3D = ..., normalizeCovar: bool = ..., ignoreHs: bool = True) -> Incomplete: ...
def ComputeCentroid(conf: Conformer, ignoreHs: bool = ..., weights: Incomplete | None = ...) -> Point3D: ...
def ComputePrincipalAxesAndMoments(conf: Conformer, ignoreHs: bool = ..., weights: None | AtomPairsParameters = ...) -> Incomplete: ...
def ComputePrincipalAxesAndMomentsFromGyrationMatrix(conf: Conformer, ignoreHs: bool = ..., weights: None | AtomPairsParameters = ...) -> Incomplete: ...
def GetAngleDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int) -> float: ...
def GetAngleRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int) -> float: ...
def GetBondLength(conf: Conformer, iAtomId: int, jAtomId: int) -> float: ...
def GetDihedralDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int) -> float: ...
def GetDihedralRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int) -> float: ...
def SetAngleDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, value: float) -> None: ...
def SetAngleRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, value: float) -> None: ...
def SetBondLength(conf: Conformer, iAtomId: int, jAtomId: int, value: float) -> None: ...
def SetDihedralDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int, value: float) -> None: ...
def SetDihedralRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int, value: float) -> None: ...
def TransformConformer(arg1: Conformer, arg2: AtomPairsParameters) -> None: ...
