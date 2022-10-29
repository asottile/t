from __future__ import annotations

import curses
import time
from typing import NamedTuple


class Button(NamedTuple):
    text: str
    top: int
    left: int
    height: int
    width: int

    @property
    def bottom(self) -> int:
        return self.top + self.height

    @property
    def right(self) -> int:
        return self.left + self.width

    @property
    def center_y(self) -> int:
        return 1 + self.top + self.height // 2

    def draw(self, stdscr: curses._CursesWindow, *, pressed: bool) -> None:
        attr = curses.A_REVERSE if pressed else 0
        for i in range(self.top, self.bottom + 1):
            if i == self.top:
                s = f'┏{(self.width - 2) * "━"}┓'
                stdscr.addstr(i, self.left, s, attr)
            elif i == self.bottom:
                s = f'┗{(self.width - 2) * "━"}┛'
                stdscr.addstr(i, self.left, s, attr)
            elif i == self.center_y:
                s = f'┃{self.text.center(self.width - 2, " ")}┃'
                stdscr.addstr(i, self.left, s, attr)
            else:
                s = f'┃{(self.width - 2) * " "}┃'
                stdscr.addstr(i, self.left, s, attr)

    def contains(self, x: int, y: int) -> bool:
        return self.top <= y <= self.bottom and self.left <= x <= self.right


A_BUTTON = Button(text='A', top=2, left=2, height=5, width=20)


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.mousemask(-1)
    curses.mouseinterval(0)

    pressed = False

    buttons = {
        Button(text='A', top=2, left=2, height=5, width=21): False,
    }

    t0 = 1
    stdscr.insstr(0, 0, 'hello world')
    while True:
        for button, pressed in buttons.items():
            button.draw(stdscr, pressed=pressed)

        c = stdscr.get_wch()
        if c == 'q':
            return 0
        elif c == curses.KEY_RESIZE:
            curses.update_lines_cols()
        elif c == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate == curses.BUTTON1_PRESSED:
                for button in buttons:
                    pressed = button.contains(x, y)
                    buttons[button] = pressed
                    if pressed:
                        t0 = time.time()
            else:
                raise AssertionError(time.time() - t0)


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
