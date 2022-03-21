import curses
import io
import os
import select
import subprocess
import sys


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.noecho()
    curses.cbreak()
    # <enter> is not transformed into '\n' so it can be differentiated from ^J
    curses.nonl()
    # ^S / ^Q / ^Z / ^\ are passed through
    curses.raw()
    stdscr.keypad(True)

    stdscr.addstr('hello world...')
    stdscr.refresh()

    proc = subprocess.Popen(
        ('bash', '-c', 'sleep 5 && echo hi'),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    stdin_fileno = sys.stdin.fileno()
    stdout_fileno = proc.stdout.fileno()
    files = (stdin_fileno, stdout_fileno)

    bio = io.BytesIO()

    while proc.poll() is None:
        rlist, _, _ = select.select(files, (), ())
        if stdout_fileno in rlist:
            bio.write(os.read(stdout_fileno, 4096))
        else:
            if stdscr.get_wch() == '\x03':  # ^C
                # TODO: more graceful terminate
                proc.terminate()
                stdscr.addstr('terminated!')
                break
    else:
        bio.write(os.read(stdout_fileno, 4096))
        stdscr.addstr(f'done! {bio.getvalue().decode()}')

    stdscr.get_wch()
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
