2024-03-13-zip-surgery
======================

I was debugging a strange bug in the `unzipper` npm package (which ended up
being a [regression in nodejs]!)

- `t.mjs`: the minimal file to show to the zip corruption
- `t.sh`: shell script to reproduce the corruption
- `t.py`: an attempt to generate a 1.0 method=deflate zip from an existing zip


[regression in nodejs]: https://youtu.be/cSd5GGrj2VA
