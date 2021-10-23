import sys


class A(object):
    def fn(self):
        print('FROM A!')


class B(A):
    def fn(self):
        print('FROM B!')


class C(B):
    def fn_super_C(self):
        return super(C, self).fn()

    def fn_super_B(self):
        return super(B, self).fn()

    def fn_super_py3(self):
        return super().fn()


def main():
    c = C()
    c.fn_super_C()
    c.fn_super_B()
    if sys.version_info > (3,):
        c.fn_super_py3()


if __name__ == '__main__':
    raise SystemExit(main())
