2024-08-16-bisecting-cpython-and-uwsgi
======================================

this is the script that I used to bisect the behaviour differences in pyuwsgi
between 3.11 and 3.12 for https://github.com/unbit/uwsgi/issues/2659

- `t.py`: the actual bisection script
- `t.sh`: to reproduce the problem standalone
- `wsgi.py`: trivial wsgi app used by `t.sh`
