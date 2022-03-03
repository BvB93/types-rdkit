import types
from collections.abc import Iterable, Iterator
from typing import Any, ClassVar, overload
from typing_extensions import Literal

from ..rdBase import _vectj
from . import Atom, AtomPairsParameters, Bond, Mol

def AddMetadataToPNGFile(metadata: dict[str, str], filename: Iterable[int]) -> Any: ...
def AddMetadataToPNGString(metadata: dict[str, str], filename: Iterable[int]) -> Any: ...
def AtomFromSmarts(SMARTS: str) -> Atom: ...
def AtomFromSmiles(SMILES: str) -> Atom: ...
def BondFromSmarts(SMARTS: str) -> Bond: ...
def BondFromSmiles(SMILES: str) -> Bond: ...

class CXSmilesFields(int):
    CX_ALL: ClassVar[CXSmilesFields]
    CX_ATOM_LABELS: ClassVar[CXSmilesFields]
    CX_ATOM_PROPS: ClassVar[CXSmilesFields]
    CX_COORDS: ClassVar[CXSmilesFields]
    CX_ENHANCEDSTEREO: ClassVar[CXSmilesFields]
    CX_LINKNODES: ClassVar[CXSmilesFields]
    CX_MOLFILE_VALUES: ClassVar[CXSmilesFields]
    CX_NONE: ClassVar[CXSmilesFields]
    CX_POLYMER: ClassVar[CXSmilesFields]
    CX_RADICALS: ClassVar[CXSmilesFields]
    CX_SGROUPS: ClassVar[CXSmilesFields]
    names: ClassVar[dict[str, CXSmilesFields]]
    values: ClassVar[dict[int, CXSmilesFields]]
    name: str

def CanonicalRankAtoms(mol: Mol, breakTies: bool = ..., includeChirality: bool = ..., includeIsotopes: bool = ...) -> _vectj: ...
def CanonicalRankAtomsInFragment(
    mol: Mol,
    atomsToUse: Iterable[int],
    bondsToUse: Iterable[int] = ...,
    atomSymbols: Iterable[int] = ...,
    breakTies: bool = ...,
    includeChirality: bool = ...,
    includeIsotopes: bool = ...,
) -> _vectj: ...
def CreateAtomBoolPropertyList(mol: Mol, propName: str, missingValueMarker: str = ..., lineSize: int = ...) -> None: ...
def CreateAtomDoublePropertyList(mol: Mol, propName: str, missingValueMarker: str = ..., lineSize: int = ...) -> None: ...
def CreateAtomIntPropertyList(mol: Mol, propName: str, missingValueMarker: str = ..., lineSize: int = ...) -> None: ...
def CreateAtomStringPropertyList(mol: Mol, propName: str, missingValueMarker: str = ..., lineSize: int = ...) -> None: ...

class ForwardSDMolSupplier:
    def __init__(self, fileobj: Any, sanitize: bool = ..., removeHs: bool = ..., strictParsing: bool = ...) -> None: ...
    def GetEOFHitOnRead(self) -> bool: ...
    def GetProcessPropertyLists(self) -> None: ...
    def SetProcessPropertyLists(self, value: bool) -> None: ...
    def atEnd(self) -> bool: ...
    def __iter__(self) -> Iterator[Mol]: ...
    def __next__(self) -> Mol: ...
    def __enter__(self) -> ForwardSDMolSupplier: ...
    def __exit__(
        self, exc_type: type[Exception] | None, exc_value: Exception | None, traceback: types.TracebackType | None
    ) -> bool: ...

class MaeMolSupplier:
    def __init__(self, fileobj: Any, sanitize: bool = ..., removeHs: bool = ...) -> None: ...
    def atEnd(self) -> bool: ...
    def __iter__(self) -> Iterator[Mol]: ...
    def __next__(self) -> Mol: ...
    def __enter__(self) -> ForwardSDMolSupplier: ...
    def __exit__(
        self, exc_type: type[Exception] | None, exc_value: Exception | None, traceback: types.TracebackType | None
    ) -> bool: ...

def MetadataFromPNGFile(filename: str) -> dict[str, bytes]: ...
def MetadataFromPNGString(filename: str) -> dict[str, bytes]: ...
def MolFragmentToCXSmarts(
    mol: Mol, atomsToUse: Iterable[int], bondsToUse: Iterable[int] = ..., isomericSmarts: bool = ...
) -> str: ...
@overload
def MolFragmentToCXSmiles(
    mol: Mol,
    params: SmilesWriteParams,
    atomsToUse: Iterable[int],
    bondsToUse: Iterable[int] = ...,
    atomSymbols: Iterable[int] = ...,
    bondSymbols: Iterable[int] = ...,
) -> str: ...
@overload
def MolFragmentToCXSmiles(
    mol: Mol,
    atomsToUse: Iterable[int],
    bondsToUse: Iterable[int] = ...,
    atomSymbols: Iterable[int] = ...,
    bondSymbols: Iterable[int] = ...,
    isomericSmarts: bool = ...,
    kekuleSmiles: bool = ...,
    rootedAtAtom: int = ...,
    canonical: bool = ...,
    allBondsExplicit: bool = ...,
    allHsExplicit: bool = ...,
) -> str: ...
def MolFragmentToSmarts(
    mol: Mol, atomsToUse: Iterable[int], bondsToUse: Iterable[int] = ..., isomericSmarts: bool = ...
) -> str: ...
@overload
def MolFragmentToSmiles(
    mol: Mol,
    params: SmilesWriteParams,
    atomsToUse: Iterable[int],
    bondsToUse: Iterable[int] = ...,
    atomSymbols: Iterable[int] = ...,
    bondSymbols: Iterable[int] = ...,
) -> str: ...
@overload
def MolFragmentToSmiles(
    mol: Mol,
    atomsToUse: Iterable[int],
    bondsToUse: Iterable[int] = ...,
    atomSymbols: Iterable[int] = ...,
    bondSymbols: Iterable[int] = ...,
    isomericSmarts: bool = ...,
    kekuleSmiles: bool = ...,
    rootedAtAtom: int = ...,
    canonical: bool = ...,
    allBondsExplicit: bool = ...,
    allHsExplicit: bool = ...,
) -> str: ...
def MolFromFASTA(text: str, sanitize: bool = ..., flavor: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = ...) -> Mol | None: ...
def MolFromHELM(text: str, sanitize: bool = ...) -> Mol | None: ...
def MolFromMol2Block(text: str, sanitize: bool = ..., removeHs: bool = ..., cleanupSubstructures: bool = ...) -> Mol | None: ...
def MolFromMol2File(
    molFileName: str, sanitize: bool = ..., removeHs: bool = ..., cleanupSubstructures: bool = ...
) -> Mol | None: ...
def MolFromMolBlock(molBlock: str, sanitize: bool = ..., removeHs: bool = ..., strictParsing: bool = ...) -> Mol | None: ...
def MolFromMolFile(molFileName: str, sanitize: bool = ..., removeHs: bool = ..., strictParsing: bool = ...) -> Mol | None: ...
def MolFromPDBBlock(
    molBlock: str, sanitize: bool = ..., removeHs: bool = ..., flavor: int = ..., proximityBonding: bool = ...
) -> Mol | None: ...
def MolFromPDBFile(
    molFileName: str, sanitize: bool = ..., removeHs: bool = ..., flavor: int = ..., proximityBonding: bool = ...
) -> Mol | None: ...
def MolFromPNGFile(filename: str, params: None | Any = ...) -> Mol | None: ...
def MolFromPNGString(png: str, params: None | Any = ...) -> Mol | None: ...
def MolFromRDKitSVG(molBlock: str, sanitize: bool = ..., removeHs: bool = ...) -> Mol | None: ...
def MolFromSequence(text: str, sanitize: bool = ..., flavor: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = ...) -> Mol | None: ...
@overload
def MolFromSmarts(SMARTS: str, mergeHs: bool = ..., replacements: dict[str, str] = ...) -> Mol | None: ...
@overload
def MolFromSmarts(SMARTS: str, params: SmartsParserParams) -> Mol | None: ...
@overload
def MolFromSmiles(SMILES: str, sanitize: bool = ..., replacements: dict[str, str] = ...) -> Mol | None: ...
@overload
def MolFromSmiles(SMILES: str, params: SmilesParserParams) -> Mol | None: ...
def MolFromTPLBlock(tplBlock: str, sanitize: bool = ..., skipFirstConf: bool = ...) -> Mol | None: ...
def MolFromTPLFile(fileName: str, sanitize: bool = ..., skipFirstConf: bool = ...) -> Mol | None: ...
def MolMetadataToPNGFile(
    mol: Mol, filename: str, includePkl: bool = ..., includeSmiles: bool = ..., includeMol: bool = ...
) -> Any: ...
def MolMetadataToPNGString(
    mol: Mol, png: str, includePkl: bool = ..., includeSmiles: bool = ..., includeMol: bool = ...
) -> Any: ...

class SmilesWriteParams: ...
class SmilesParserParams: ...
class SmartsParserParams: ...
