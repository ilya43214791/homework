import pytest
import homework_function_receives_some
def test_function_receives_value():
        test_value = "rasf"
        with pytest.raises(AssertionError):
            assert homework_function_receives_some.function_receives_value(test_value) is str


def test_function_receives_value_bool():
    test_value = 12
    with pytest.raises(TypeError):
        assert homework_function_receives_some.function_receives_value(test_value) is int

def test_function_receives_value_zero():
    test_value = 0
    with pytest.raises(TypeError):
        assert homework_function_receives_some.function_receives_value(test_value) is int


def test_function_receives_value_set():
    test_value = set("grewr")
    with pytest.raises(AssertionError):
        assert homework_function_receives_some.function_receives_value(test_value) is set


def test_function_receives_value_float():
    test_value = 423.143
    with pytest.raises(TypeError):
        assert homework_function_receives_some.function_receives_value(test_value) is float