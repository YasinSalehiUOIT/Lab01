def main():
    cost_per_item = 19.99
    quantity = 5 

    # Part 1: Calculate subtotal, tax, and total cost
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # Part 2: Print values of all variables
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # Part 3: Fixing the error in the commented out code
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    # The error here is that investment is a float and cannot be concatenated with a string directly.
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')  # Fixed by converting investment to string.

if __name__ == "__main__":
    main()
