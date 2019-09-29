import contextlib
import curses
import os

Q_TO_QUIT = 'press q to quit'


def c_main(stdscr):
    stdscr.insstr(curses.LINES - 1, curses.COLS - len(Q_TO_QUIT), Q_TO_QUIT)
    stdscr.move(0, 0)
    i = 0
    while True:
        wch = stdscr.get_wch()
        if wch == '\033':
            stdscr.nodelay(True)
            try:
                while True:
                    try:
                        wch += stdscr.get_wch()
                    except curses.error:
                        break
            finally:
                stdscr.nodelay(False)
        if isinstance(wch, str) and len(wch) > 1:
            stdscr.insstr(i, 0, f'(sequence) {wch!r}')
        else:
            key = wch if isinstance(wch, int) else ord(wch)
            keyname = curses.keyname(key)
            stdscr.insstr(i, 0, f'{wch!r} {key!r} {keyname.decode()!r}')
        i += 1
        stdscr.move(i, 0)
        if wch == 'q':
            return


def _init_screen():
    os.environ.setdefault('ESCDELAY', '25')
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    # <enter> is not transformed into '\n' so it can be differentiated from ^J
    curses.nonl()
    # ^S / ^Q / ^Z / ^\ are passed through
    curses.raw()
    stdscr.keypad(True)
    return stdscr


@contextlib.contextmanager
def make_stdscr():
    """essentially `curses.wrapper` but split out to implement ^Z"""
    stdscr = _init_screen()
    try:
        yield stdscr
    finally:
        curses.endwin()


def main() -> int:
    with make_stdscr() as stdscr:
        c_main(stdscr)
    return 0


if __name__ == '__main__':
    exit(main())
