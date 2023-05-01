import pytest
@pytest.mark.fast
def test_my_fast_test():
    sdu = "Nazar"
    assert "az" in sdu

def test_number():
    number = 100
    assert 90+10 == number