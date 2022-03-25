from __future__ import annotations


class mcs(type):
    def __new__(cls, name, bases, dct):
        dct['__module__'] = 'pytest'
        return super().__new__(cls, name, bases, dct)


class C(metaclass=mcs):
    pass


class D(C):
    pass


def main():
    print(C.__module__)
    print(D.__module__)


if __name__ == '__main__':
    raise SystemExit(main())
