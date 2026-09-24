class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        one_dollar = float(input("How many dollars?: "))
        half_dollar = float(input("How many half dollars?: "))
        quarter = float(input("How many quarters?: "))
        nickle = float(input("How many nickles?: "))

        total = (one_dollar * 1.00) + (half_dollar * 0.05) + (quarter * 0.25) + (nickle * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = max(0.0,cost - coins)
            print(f"Here is ${change: .2f} in change.")
            return True
