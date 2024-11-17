import employee_info


def test_calc_avg_salary():

    expected_avg = (50000+60000+56000+70000+65000+60000)/6
    result_avg = employee_info.calculate_average_salary()

    assert(expected_avg == result_avg)

def test_age():
    lower_limit=20
    upper_limit=30

    expected_result= [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    result = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    assert(expected_result == result)

def test_get_employee_dept():
    expected_result = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    test_department = "Marketing"
    result = employee_info.get_employees_by_dept(test_department)

    assert(expected_result == result)