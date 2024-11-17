from Lab2 import bmi as bmi

def test_bmi_normal_weight():
    excepted_result = 0
    test_bmi = bmi.calculate_bmi(height=1.73,weight=65)
    assert(excepted_result == test_bmi)
def test_bmi_over_weight():
    excepted_result = 1
    test_bmi = bmi.calculate_bmi(height=1.73,weight=80)
    assert(excepted_result == test_bmi)

def test_bmi_under_weight():
    excepted_result = -1
    test_bmi = bmi.calculate_bmi(height=1.73,weight=55)
    assert(excepted_result == test_bmi)
