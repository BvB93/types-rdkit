from typing import Any

class Point3D:
    def __getattr__(self, name: str) -> Any: ...

class Point2D:
    def __getattr__(self, name: str) -> Any: ...
