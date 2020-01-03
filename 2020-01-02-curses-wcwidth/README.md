curses-wcwidth
==============

an implementation of `wcwidth(...)` for usage with curses.  `wcwidth` is used
to determine how wide a character it is (for curses: how many cells it will
take up when rendered).

after coming up with this, I did some research and apparently this is how
`lynx` computes `wcwidth` to do rendering.

the rendered output looks something like this:

```
C       WIDTH   NAME
====================================
☃       1       SNOWMAN                                                         ​
        0       ZERO WIDTH SPACE
🙃      2       UPSIDE-DOWN FACE
x       1       LATIN SMALL LETTER X
```
