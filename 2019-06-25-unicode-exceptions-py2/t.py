from __future__ import annotations

import unittest

PY2 = str is bytes


def f():
    raise Exception('\u2603')


class MyTest(unittest.TestCase):
    def test_thing(self):
        if PY2:
            assert_raises_regex = self.assertRaisesRegexp
        else:
            assert_raises_regex = self.assertRaisesRegex
        assert_raises_regex(Exception, '\u2603', f)


if __name__ == '__main__':
    unittest.main()
