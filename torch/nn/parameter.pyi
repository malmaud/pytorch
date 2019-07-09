from typing import Any
from .. import Tensor

class Parameter(Tensor):
    def __new__(cls, data: Any=None, requires_grad: bool=...): ...
