import pytest

def bit1error():
	raise SystemExit()

def bit2error():
	return 2

def test_bit1():
	with pytest.raises(SystemExit):
		bit1error()

def test_bit2():
	assert bit2error() == 1