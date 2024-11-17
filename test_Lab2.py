from Lab2 import lab2

def test_find_min_max():
    test_list = [1,3,4,5,6,78,8,9,0]
    test_max = max(test_list)
    test_min = min(test_list)

    result_max = lab2.calc_max(test_list)
    result_min = lab2.calc_min(test_list)

    assert(test_max == result_max)
    assert(test_min == result_min)

def test_calc_avg():
    test_list = [1,3,4,5,6,78,8,9,0]
    test_avg = sum(test_list)/ len(test_list)

    result_avg = lab2.calc_avg(test_list)

    assert(test_avg == result_avg)

def test_median():
    test_list = [1,3,4,5,6,78,8,9,0]
    sorted_list = sorted(test_list)
    n = len(sorted_list)
    if n % 2 == 1:
        middle_index = n//2
        median = sorted_list[middle_index]
    else:
        midvalue1 = n//2
        midvalue2 = n//2-1
        median = (sorted_list[midvalue1] + sorted_list[midvalue2])/2
        
    result_median = lab2.calc_median(test_list)
    assert(median == result_median)

