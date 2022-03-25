from __future__ import annotations

import curses
import unicodedata

CHARS = '\u2603\u200b\U0001f643x'


def wcwidth(c: str) -> int:
    try:
        win = wcwidth._window  # type: ignore
    except AttributeError:
        win = wcwidth._window = curses.newwin(1, 10)  # type: ignore

    win.addstr(0, 0, c)
    _, x = win.getyx()
    return x


def c_main(stdscr: curses._CursesWindow) -> None:
    stdscr.addstr(1, 0, 'C\tWIDTH\tNAME')
    stdscr.addstr(2, 0, '====================================')
    for i, c in enumerate(CHARS):
        stdscr.addstr(i + 3, 0, f'{c}\t{wcwidth(c)}\t{unicodedata.name(c)}')
    stdscr.get_wch()


if __name__ == '__main__':
    curses.wrapper(c_main)
