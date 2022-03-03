from collections.abc import Iterable
from typing import Any, ClassVar

from .rdMolDescriptors import AtomPairsParameters
from ..Geometry import Point3D, Point2D
from ..rdBase import _vectj, _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
from .._typing import _VectBase, _SeqBase, _SupportsLenAndGetitem

class Mol:
    def AddConformer(self, mol: Mol, sgroup: SubstanceGroup) -> None: ...
    def ClearComputedProps(self, includeRings: bool = ...) -> None: ...
    def ClearProp(self, key: str) -> None: ...
    def Compute2DCoords(self, canonOrient: bool = ..., clearConfs: bool = ..., coordMap: dict[int, Point2D] = ..., nFlipsPerSample: int = ..., nSample: int = ..., sampleSeed: int = ..., permuteDeg4Nodes: bool = ..., bondLength: float = ..., forceRDKit: bool) -> int: ...
    def ComputeGasteigerCharges(self, nIter: int = ..., throwOnParamFailure: bool = ...) -> None: ...
    def Debug(self, useStdout: bool = ...) -> None: ...
    def GetAromaticAtoms(self) -> _ROQAtomSeq: ...
    def GetAtomWithIdx(self, idx: int) -> Atom: ...
    def GetAtoms(self) -> _ROAtomSeq: ...
    def GetAtomsMatchingQuery(self, query: QueryAtom) -> _ROQAtomSeq: ...
    def GetBondBetweenAtoms(self, idx1: int, idx2: int) -> Bond: ...
    def GetBondWithIdx(self, idx: int) -> Bond: ...
    def GetBonds(self) -> _ROBondSeq: ...
    def GetBoolProp(self, key: str) -> bool: ...
    def GetConformer(self, id: int) -> Conformer: ...
    def GetConformers(self) -> _ROConformerSeq: ...
    def GetDoubleProp(self, key: str) -> float: ...
    def GetIntProp(self, key: str) -> int: ...
    def GetNumAtoms(self, onlyHeavy: int = ..., onlyExplicit: bool = ...) -> int: ...
    def GetNumBonds(self, onlyHeavy: int = ...) -> int: ...
    def GetNumConformers(self) -> int: ...
    def GetNumHeavyAtoms(self) -> int: ...
    def GetProp(self, key: str) -> str: ...
    def GetPropNames(self, includePrivate: bool = ..., includeComputed: bool = ...) -> _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE: ...
    def GetPropsAsDict(self, includePrivate: bool = ..., includeComputed: bool = ...) -> dict[str, Any]: ...
    def GetRingInfo(self) -> RingInfo: ...
    def GetStereoGroups(self) -> StereoGroup_vect: ...
    def GetSubstructMatch(self, query: Mol, useChirality: bool = ..., useQueryQueryMatches: bool = ...) -> tuple[int, ...]: ...
    def GetSubstructMatches(self, query: Mol, uniquify: bool = ..., useChirality: bool = ..., useQueryQueryMatches: bool = ..., maxMatches: int = ...) -> tuple[tuple[int, ...], ...]: ...
    def GetUnsignedProp(self, key: str) -> int: ...
    def HasProp(self, key: str) -> int: ...
    def HasSubstructMatch(self, query: Mol, recursionPossible: bool = ..., useChirality: bool = ..., useQueryQueryMatches: bool = ...) -> bool: ...
    def NeedsUpdatePropertyCache(self) -> bool: ...
    def RemoveAllConformers(self) -> None: ...
    def RemoveConformer(self, id: int) -> None: ...
    def SetBoolProp(self, key: str, val: bool, computed: bool = ...) -> None: ...
    def SetDoubleProp(self, key: str, val: float, computed: bool = ...) -> None: ...
    def SetIntProp(self, key: str, val: int, computed: bool = ...) -> None: ...
    def SetProp(self, key: str, val: str, computed: bool = ...) -> None: ...
    def SetUnsignedProp(self, key: str, val: int, computed: bool = ...) -> None: ...
    def ToBinary(self) -> bytes: ...
    def UpdatePropertyCache(self, strict: bool = ...) -> None: ...
    __instance_size__: int
    __safe_for_unpickling__: bool

def GetMolSubstanceGroups(arg1: Mol, /) -> SubstanceGroup_VECT: ...

class SubstanceGroup_VECT(_VectBase[SubstanceGroup]): ...
class StereoGroup_vect(_VectBase[StereoGroup]): ...

class _ROQAtomSeq(_SeqBase[Atom]): ...
class _ROAtomSeq(_SeqBase[Atom]): ...
class _ROBondSeq(_SeqBase[Bond]): ...
class _ROConformerSeq(_SeqBase[Conformer]): ...

class Atom:
    def __init__(self, value: int | str | Atom) -> None: ...
    def ClearProp(self, key: str) -> None: ...
    def DescribeQuery(self) -> str: ...
    def GetAtomMapNum(self) -> int: ...
    def GetAtomicNum(self) -> int: ...
    def GetBonds(self) -> tuple[Bond, ...]: ...
    def GetBoolProp(self, key: str) -> bool: ...
    def GetChiralTag(self) -> ChiralType: ...
    def GetDegree(self) -> int: ...
    def GetDoubleProp(self, key: str) -> float: ...
    def GetExplicitBitVectProp(self, key: str) -> ExplicitBitVect: ...
    def GetExplicitValence(self) -> int: ...
    def GetFormalCharge(self) -> int: ...
    def GetHybridization(self) -> HybridizationType: ...
    def GetIdx(self) -> int: ...
    def GetImplicitValence(self) -> int: ...
    def GetIntProp(self, key: str) -> int: ...
    def GetIsAromatic(self) -> bool: ...
    def GetIsotope(self) -> int: ...
    def GetMass(self) -> float: ...
    def GetMonomerInfo(self) -> None | AtomMonomerInfo: ...
    def GetNeighbors(self) -> tuple[Atom ,...]: ...
    def GetNoImplicit(self) -> bool: ...
    def GetNumExplicitHs(self) -> int: ...
    def GetNumImplicitHs(self) -> int: ...
    def GetNumRadicalElectrons(self) -> int: ...
    def GetOwningMol(self) -> Mol: ...
    def GetPDBResidueInfo(self) -> AtomPDBResidueInfo: ...
    def GetProp(self, key: str) -> str: ...
    def GetPropNames(self, includePrivate: bool = ..., includeComputed: bool = ...) -> _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE: ...
    def GetPropsAsDict(self, includePrivate: bool = ..., includeComputed: bool = ...) -> dict[str, Any]: ...
    def GetSmarts(self, doKekule: bool = ..., allHsExplicit: bool = ..., isomericSmiles: bool = ...) -> str: ...
    def GetSymbol(self) -> str: ...
    def GetTotalDegree(self) -> int: ...
    def GetTotalNumHs(self, includeNeighbors: bool = ...) -> int: ...
    def GetTotalValence(self) -> int: ...
    def GetUnsignedProp(self, key: str) -> int: ...
    def HasOwningMol(self) -> bool: ...
    def HasProp(self, key: str) -> bool: ...
    def HasQuery(self) -> bool: ...
    def InvertChirality(self) -> None: ...
    def IsInRing(self) -> bool: ...
    def IsInRingSize(self, size: int) -> bool: ...
    def Match(self, other: Atom) -> bool: ...
    def NeedsUpdatePropertyCache(self) -> bool: ...
    def SetAtomMapNum(self, mapno: int, strict: bool = ...) -> None: ...
    def SetAtomicNum(self, value: int) -> None: ...
    def SetBoolProp(self, key: str, value: bool) -> None: ...
    def SetChiralTag(self, tag: ChiralType) -> None: ...
    def SetDoubleProp(self, key: str, value: float) -> None: ...
    def SetExplicitBitVectProp(self, key: str, value: ExplicitBitVect) -> None: ...
    def SetFormalCharge(self, value: int) -> None: ...
    def SetHybridization(self, value: HybridizationType) -> None: ...
    def SetIntProp(self, key: str, value: int) -> None: ...
    def SetIsAromatic(self, value: bool) -> None: ...
    def SetIsotope(self, value: int) -> None: ...
    def SetMonomerInfo(self, value: AtomMonomerInfo) -> None: ...
    def SetNoImplicit(self, value: bool) -> None: ...
    def SetNumExplicitHs(self, value: int) -> None: ...
    def SetNumRadicalElectrons(self, value: int) -> None: ...
    def SetPDBResidueInfo(self, value: AtomMonomerInfo) -> None: ...
    def SetProp(self, key: str, value: str) -> None: ...
    def SetUnsignedProp(self,key: str, value: int) -> None: ...
    def UpdatePropertyCache(self, strict: bool = ...) -> None: ...

class Bond:
    def __getattr__(self, name: str) -> Any: ...

class Bracket:  # ?
    def __getattr__(self, name: str) -> Any: ...

class SubstanceGroupAttach:
    @property
    def aIdx(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def lvIdx(self) -> int: ...

class ExplicitBitVect:  # ?
    ...

class QueryAtom(Atom):
    def ExpandQuery(self, other: QueryAtom, how: CompositeQueryType = ...,, maintainOrder: bool = ...) -> None: ...
    def SetQuery(self, other: QueryAtom) -> None: ...

class Conformer:
    def __init__(self, value: int | Conformer = ...) -> None: ...
    def ClearComputedProps(self) -> None: ...
    def ClearProp(self, key: str) -> None: ...
    def GetAtomPosition(self, idx: int) -> Point3D: ...
    def GetBoolProp(self, key: str) -> bool: ...
    def GetDoubleProp(self, key: str) -> bool: ...
    def GetId(self) -> int: ...
    def GetIntProp(self, key: str) -> int: ...
    def GetNumAtoms(self) -> int: ...
    def GetOwningMol(self) -> Mol: ...
    def GetPositions(self) -> None: ...
    def GetProp(self, key: str) -> str: ...
    def GetPropNames(self, includePrivate: bool = ..., includeComputed: bool = ...) -> _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE: ...
    def GetPropsAsDict(self, includePrivate: bool = ..., includeComputed: bool = ...) -> dict[str, Any]: ...
    def GetUnsignedProp(self, key: str) -> int: ...
    def HasOwningMol(self) -> bool: ...
    def HasProp(self, key: str) -> bool: ...
    def Is3D(self) -> bool: ...
    def Set3D(self, value: bool) -> None: ...
    def SetAtomPosition(self, value: int, prm: AtomPairsParameters) -> None: ...
    def SetBoolProp(self, key: str, value: bool, computed: bool = ...) -> None: ...
    def SetDoubleProp(self, key: str, value: float, computed: bool = ...) -> None: ...
    def SetId(self) -> None: ...
    def SetIntProp(self, key: str, value: int, computed: bool = ...) -> None: ...
    def SetProp(self, key: str, value: str, computed: bool = ...) -> None: ...
    def SetUnsignedProp(self, key: str, value: int, computed: bool = ...) -> None: ...

class RingInfo:
   def AddRing(self, atomIndices: _SupportsLenAndGetitem[int], bondIndices: _SupportsLenAndGetitem[int]) -> None: ...
   def AreRingFamiliesInitialized(self) -> bool: ...
   def AtomRingFamilies(self) -> tuple[tuple[int, ...], ...]: ...
   def AtomRings(self) -> tuple[tuple[int, int], ...]: ...
   def BondRingFamilies(self) -> tuple[tuple[int, ...], ...]: ...
   def BondRings(self) -> tuple[tuple[int, int], ...]: ...
   def IsAtomInRingOfSize(self, idx: int, size: int) -> bool: ...
   def IsBondInRingOfSize(self, idx: int, size: int) -> bool: ...
   def MinAtomRingSize(self, idx: int) -> int: ...
   def MinBondRingSize(self, idx: int) -> int: ...
   def NumAtomRings(self, idx: int) -> int: ...
   def NumBondRings(self, idx: int) -> int: ...
   def NumRelevantCycles(self) -> int: ...
   def NumRingFamilies(self) -> int: ...
   def NumRings(self) -> int: ...

class StereoGroup:
    def GetAtoms(self) -> tuple[Atom, ...]: ...
    def GetGroupType(self) -> StereoGroupType: ...

class AtomMonomerInfo:
    def _init__(self, type: AtomMonomerType = ..., name: str = ...) -> None: ...
    def GetMonomerType(self) -> AtomMonomerType: ...
    def GetName(self) -> str: ...
    def SetMonomerType(self, type: AtomMonomerType) -> None: ...
    def SetName(self, name: str) -> None: ...

class AtomPDBResidueInfo(AtomMonomerInfo):
    def __init__(self, atomName: str = ..., serialNumber: int = ..., altLoc: str = ..., residueName: str = ..., residueNumber: int = ..., chainId: str = ..., insertionCode: str = ..., occupancy: float = ..., tempFactor: float = ..., isHeteroAtom: bool = ..., secondaryStructure: int = ..., segmentNumber: int = ...) -> None: ...
    def GetAltLoc(self) -> str: ...
    def GetChainId(self) -> str: ...
    def GetInsertionCode(self) -> str: ...
    def GetIsHeteroAtom(self) -> bool: ...
    def GetOccupancy(self) -> float: ...
    def GetResidueName(self) -> str: ...
    def GetResidueNumber(self) -> int: ...
    def GetSecondaryStructure(self) -> int: ...
    def GetSegmentNumber(self) -> int: ...
    def GetSerialNumber(self) -> int: ...
    def GetTempFactor(self) -> float: ...
    def SetAltLoc(self, value: str) -> None: ...
    def SetChainId(self, value: str) -> None: ...
    def SetInsertionCode(self, value: str) -> None: ...
    def SetIsHeteroAtom(self, value: bool) -> None: ...
    def SetOccupancy(self, value: float) -> None: ...
    def SetResidueName(self, value: str) -> None: ...
    def SetResidueNumber(self, value: int) -> None: ...
    def SetSecondaryStructure(self, value: int) -> None: ...
    def SetSegmentNumber(self, value: int) -> None: ...
    def SetSerialNumber(self, value: int) -> None: ...
    def SetTempFactor(self, value: float) -> None: ...

class CompositeQueryType(int):
    COMPOSITE_AND: ClassVar[CompositeQueryType]
    COMPOSITE_OR: ClassVar[CompositeQueryType]
    COMPOSITE_XOR: ClassVar[CompositeQueryType]
    names: ClassVar[dict[str, StereoGroupType]]
    values: ClassVar[dict[int, StereoGroupType]]
    name: str

class StereoGroupType(int):
    STEREO_ABSOLUTE: ClassVar[StereoGroupType]
    STEREO_AND: ClassVar[StereoGroupType]
    STEREO_OR: ClassVar[StereoGroupType]
    names: ClassVar[dict[str, StereoGroupType]]
    values: ClassVar[dict[int, StereoGroupType]]
    name: str

class AtomMonomerType(int):
    UNKNOWN: ClassVar[AtomMonomerType]
    PDBRESIDUE: ClassVar[AtomMonomerType]
    OTHER: ClassVar[AtomMonomerType]
    names: ClassVar[dict[str, AtomMonomerType]]
    values: ClassVar[dict[int, AtomMonomerType]]
    name: str

class ChiralType(int):
    CHI_OTHER: ClassVar[ChiralType]
    CHI_TETRAHEDRAL_CCW: ClassVar[ChiralType]
    CHI_TETRAHEDRAL_CW: ClassVar[ChiralType]
    CHI_UNSPECIFIED: ClassVar[ChiralType]
    names: ClassVar[dict[str, ChiralType]]
    values: ClassVar[dict[int, ChiralType]]
    name: str

class HybridizationType(int):
    UNSPECIFIED: ClassVar[HybridizationType]
    S: ClassVar[HybridizationType]
    SP: ClassVar[HybridizationType]
    SP2: ClassVar[HybridizationType]
    SP3: ClassVar[HybridizationType]
    SP3D: ClassVar[HybridizationType]
    SP3D2: ClassVar[HybridizationType]
    OTHER: ClassVar[HybridizationType]
    names: ClassVar[dict[str, HybridizationType]]
    values: ClassVar[dict[int, HybridizationType]]
    name: str

class SubstanceGroup:
    def AddAtomWithBookmark(self, __mark: int) -> None: ...
    def AddAtomWithIdx(self, __idx: int) -> None: ...
    def AddAttachPoint(self, __aldx: int, __lvldx: int, __idStr: str) -> None: ...
    def AddBondWithBookmark(self, __mark: int) -> None: ...
    def AddBondWithIdx(self, __idx: int) -> None: ...
    def AddBracket(self, __bracket: Bracket) -> None: ...
    def AddCState(self, __bondIdx: int, vector: Point3D) -> None: ...
    def AddParentAtomWithBookmark(self, __mark: int) -> None: ...
    def AddParentAtomWithIdx(self, __idx: int) -> None: ...
    def ClearAttachPoints(self) -> None: ...
    def ClearBrackets(self) -> None: ...
    def ClearCStates(self) -> None: ...
    def ClearProp(self) -> None: ...
    def GetAtoms(self) -> _vectj: ...
    def GetAttachPoints(self) -> tuple[SubstanceGroupAttach, ...]: ...
    def GetBonds(self) -> _vectj: ...
    def GetBoolProp(self, __name: str) -> bool: ...
    def GetBrackets(self) -> tuple[Any, ...]: ...
    def GetCStates(self) -> tuple[Any, ...]: ...
    def GetDoubleProp(self, __name: str) -> float: ...
    def GetIndexInMol(self) -> int: ...
    def GetIntProp(self, __name: str) -> int: ...
    def GetOwningMol(self) -> Mol: ...
    def GetParentAtoms(self) -> _vectj: ...
    def GetProp(self, __name: str) -> str: ...
    def GetPropNames(self) -> _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE: ...
    def GetPropsAsDict(self) -> dict[str, Any]: ...
    def GetStringVectProp(self, __name: str) -> _vectNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE: ...
    def GetUnsignedProp(self, __name: str) -> int: ...
    def GetUnsignedVectProp(self, __name: str) -> _vectj: ...
    def HasProp(self, __name: str) -> bool: ...
    def SetAtoms(self, __atoms: Iterable[int]) -> None: ...
    def SetBonds(self, __bonds: Iterable[int]) -> None: ...
    def SetBoolProp(self, __name: str, __value: bool) -> None: ...
    def SetDoubleProp(self, __name: str, __value: float) -> None: ...
    def SetIntProp(self, __name: str, __value: int) -> None: ...
    def SetParentAtoms(self, __patoms: Iterable[int]) -> None: ...
    def SetProp(self, __name: str, __value: str) -> None: ...
    def SetUnsignedProp(self, __name: str, __value: int) -> None: ...