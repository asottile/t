from typing import Optional


class C:
    def __init__(self) -> None:
        self.x = None  # type: Optional[int]

    def set_x(self, x: int) -> None:
        self.x = x

    def use_x(self) -> int:
        assert self.x is not None  # convince mypy that lateinit has occurred
        return self.x + 5
