import struct

# figure out offsets using `zipdetails

contents = open('qq/plugin-build/build/distributions/sentry-android-gradle-plugin-4.3.0.zip', 'rb').read()  # noqa: E501
# local file header for directory
h1 = contents[:0x43]
# local file header for deflated xml
h2 = contents[0x34CD91E:0x34CDC78]
# central header for directory
c1 = bytearray(contents[0x34CDFB7:0x34CE008])
c1[42:46] = struct.pack('i', 0)  # position of local file header
# central header for deflated xml
c2 = bytearray(contents[0x34CE17D:0x34CE1DD])
c2[42:46] = struct.pack('i', len(h1))  # position of local file header

end = bytearray(contents[0x34CE239:])
end[8] = end[10] = 0x02
end[12:16] = struct.pack('i', len(c1) + len(c2))
end[16:20] = struct.pack('i', len(h1) + len(h2))

with open('fakezip.zip', 'wb') as f:
    f.write(h1 + h2)
    f.write(c1)
    f.write(c2)
    f.write(end)
