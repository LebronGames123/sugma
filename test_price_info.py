import price_info

def test_total_cost_shopping():

    test_price = 46.75
    result = price_info.total_cost_shopping()

    assert(result == test_price)

def test_cost_of_fruits():
    test_quantity = 5
    test_fruit = 'apple'
    test_cost = (5*1.20)

    result = price_info.cost_of_fruits(test_fruit,test_quantity)