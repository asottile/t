import time


def main() -> int:
    TIME = 600

    t0 = int(time.monotonic())
    while time.monotonic() < t0 + TIME:
        time.sleep(.5)
        time_left = TIME - (int(time.monotonic()) - t0)
        minutes = time_left // 60
        seconds = time_left % 60
        print(f'\r{minutes:02}:{seconds:02}', end='')
    print()


if __name__ == '__main__':
    raise SystemExit(main())
