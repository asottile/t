cancellable background task in curses
=====================================

this was made while investigating implementing linters for babi.

unfortunately, this approach only works on posixlikes because windows
`select` only works for sockets.
