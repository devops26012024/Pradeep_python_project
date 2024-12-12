from app import add, multiply

def test_end_to_end():
    result1 = add(1, 2)
    result2 = multiply(result1, 3)
    assert result2 == 9
