### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print("Sorry there is not enough" + item + ".")
                return False
            else:
                return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        one_dollar = float(input("How many dollars?: "))
        half_dollar = float(input("How many half dollars?: "))
        quarter = float(input("How many quarters?: "))
        nickle = float(input("How many nickles?: "))

        total = (one_dollar * 1.00) + (half_dollar * 0.05) + (quarter * 0.25)+ (nickle * 0.05)
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


        ### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)
while True:
        prompt = input("What would you like? (small/medium/large/off/report): ")
        if prompt == "off":
            exit()
        elif prompt == "report":
            print(f"Bread: {resources["bread"]} slice(s)")
            print(f"Ham: {resources["ham"]} slice(s)")
            print(f"Cheese: {resources["cheese"]} ounce(s)")
        elif prompt in recipes:
            sandwich = recipes[prompt]
            if machine.check_resources(sandwich ["ingredients"]):
                coins_inserted = machine.process_coins()
                if machine.transaction_result(coins_inserted, sandwich["cost"]):
                    machine.make_sandwich(prompt, sandwich ["ingredients"])
        else: print("Invaild input. Please try again.")
