from __future__ import annotations

import cProfile
import importlib.metadata
import sys


def main() -> int:
    ep_name = sys.argv.pop(1)
    ep, = {
        ep
        for dist in importlib.metadata.distributions()
        for ep in dist.entry_points
        if ep.group == 'console_scripts' and ep.name == ep_name
    }
    main = ep.load()
    with cProfile.Profile() as prof:
        ret = main()
    prof.dump_stats('log.pstats')
    return ret


if __name__ == '__main__':
    raise SystemExit(main())
