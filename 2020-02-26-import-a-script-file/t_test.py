import importlib.machinery
import importlib.util


def _import_file(s):
    modname = s.replace('/', '_')
    loader = importlib.machinery.SourceFileLoader(f'_{modname}', s)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


t = _import_file('t')


def test_main(capsys):
    ret = t.main(('Anthony',))
    assert ret == 0
    out, err = capsys.readouterr()
    assert out == 'Hello Anthony\n'
    assert err == ''
