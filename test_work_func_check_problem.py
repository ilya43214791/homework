import pytest
import work_func_check_problem

def test_import_mile_in_km():
    test_value = 20.4
    with pytest.raises(AssertionError):
        assert work_func_check_problem.import_mile_in_km(test_value) == 4.1

def test_import_mile_in_str():
    test_value = "check"
    with pytest.raises(TypeError):
        assert work_func_check_problem.import_mile_in_km(test_value)

def test_import_mile_in_negativ_int():
    test_value = -64
    assert work_func_check_problem.import_mile_in_km(test_value)

def test_import_mile_in_negativ_zero():
    test_value = 0
    with pytest.raises(AssertionError):
        assert work_func_check_problem.import_mile_in_km(test_value)

def test_import_mile_in__int():
    test_value = 453
    assert work_func_check_problem.import_mile_in_km(test_value)