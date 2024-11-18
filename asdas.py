import csv

def is_price_range_valid(price_lower_limit, price_upper_limit):
    try:
        lower_limit = int(price_lower_limit)
        upper_limit = int(price_upper_limit)
        return lower_limit <= upper_limit
    except ValueError:
        return False

def calc_average_expenses(csv_list):
    total = sum(float(item["price"]) for item in csv_list)
    average = total / len(csv_list)
    return average

def calc_total_expenses(csv_list):
    total_expenses = sum(float(item["price"]) for item in csv_list)
    return total_expenses

def get_items_by_price_range(csv_list, str_price_lower_limit, str_price_upper_limit):
    lower_limit = int(str_price_lower_limit)
    upper_limit = int(str_price_upper_limit)

    result = [
        item for item in csv_list
        if lower_limit <= float(item["price"]) <= upper_limit
    ]
    return result

def sort_by_items(csv_list):
    result = sorted(csv_list, key=lambda x: x["expense_item"])
    return result

def display_main_menu():
    print("\n----- Expense Tracker -----")
    print("Select option\n")
    print("1 - Display all records")
    print("2 - Display statistics")
    print("3 - Display items within price range")
    print("Q - Quit")

    option = input("Enter selection =>")
    csv_list = load_csv_database()

    if option == '1':
        display_all_records(csv_list)
    elif option == '2':
        get_expenses_statistics(csv_list)
    elif option == '3':
        price_lower_limit = input("Price (Lower Limit) = ")
        price_upper_limit = input("Price (Upper Limit) = ")
        if is_price_range_valid(price_lower_limit, price_upper_limit):
            result_list = get_items_by_price_range(csv_list, price_lower_limit, price_upper_limit)
            display_results(result_list)
        else:
            print("\nInvalid Price Range entered!")
    elif option == 'Q':
        print("Thank You and have a nice day :-)")
        quit()

def load_csv_database():
    print("\nLoading CSV file database")
    with open('expenses.csv', mode='r') as csv_file:
        csv_dict = csv.DictReader(csv_file)
        return list(csv_dict)

def display_results(result_list):
    for item in result_list:
        print(f"{item['date']}\t\t{item['expense_item']}\t\t${float(item['price']):.2f}")

def display_all_records(csv_list):
    print("Date\t\t\tExpense Item\t\tPrice")
    for item in csv_list:
        print(f"{item['date']}\t\t{item['expense_item']}\t\t\t\t${float(item['price']):.2f}")

def get_expenses_statistics(csv_list):
    print("\nExpenses Statistics")
    print("-------------------")
    print("Total Expenses = $" + str(calc_total_expenses(csv_list)))
    print("Average Expenses = $" + str(calc_average_expenses(csv_list)))

def main():
    while True:
        display_main_menu()

if __name__ == "__main__":
    main()
