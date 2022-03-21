from __future__ import annotations

import curses
import itertools
import time


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.curs_set(0)

    s = 'hello hello chat, this is a marquee'
    s = f'{s:<{curses.COLS}}'[::-1]
    stdscr.addstr(s[::-1])

    for c in itertools.cycle(s):
        time.sleep(.05)
        stdscr.insstr(0, 0, c)
        stdscr.refresh()

    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
