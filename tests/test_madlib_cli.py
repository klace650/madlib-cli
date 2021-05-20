from madlib_cli.madlib_cli import prove_it
from madlib_cli import __version__


def test_version():
    assert __version__ == '0.1.0'

prove_it()