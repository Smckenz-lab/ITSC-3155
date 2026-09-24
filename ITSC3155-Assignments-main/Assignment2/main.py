import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()





def main():
    is_on = True
    while is_on:
        prompt = input("What would you like? (small/medium/large/off/report): ")
        if prompt == "off":
            is_on = False
        elif prompt == "report":
            print(f"Bread: {resources["bread"]} slice(s)")
            print(f"Ham: {resources["ham"]} slice(s)")
            print(f"Cheese: {resources["cheese"]} ounce(s)")
        elif prompt in recipes:
            sandwich = recipes[prompt]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(prompt, sandwich["ingredients"])
        else:
            print("Invaild input. Please try again.")

if __name__=="__main__":
    main()
