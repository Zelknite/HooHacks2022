import pytest

def bit1error():
    raise SystemExit()

def test_mytest():
    with pytest.raises(SystemExit):
        bit1error()