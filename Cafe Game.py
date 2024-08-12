import random
import time

# Define the customers and their orders
customers = [
    {"name": "Alice", "order": "coffee"},
    {"name": "Bob", "order": "tea"},
    {"name": "Charlie", "order": "cake"},
    {"name": "Diana", "order": "crepes"},
    {"name": "Eve", "order": "sandwich"},
    {"name": "Mina", "order": "brownie"},
    {"name": "Carlos", "order": "sugar cookie"},
    {"name": "Ben", "order": "fruit cup"}
]

# Define the responses and coin values
orders = ["coffee", "tea", "cake", "crepes", "sandwich", "brownie", "sugar cookie", "fruit cup"]
coin_values = {
    "coffee": 5,
    "tea": 4,
    "cake": 6
}

# Function to serve a customer
def serve_customer(customer_order, served_order):
    if customer_order == served_order:
        return coin_values[served_order], "happy"
    else:
        return coin_values[served_order] // 2, "not happy"

def game():
    coins = 0
    print("Welcome to the Cafe Game!")
    print("You will be serving customers and earning coins based on your performance.")
    
    random.shuffle(customers)  # Shuffle customers to randomize the order
    
    for customer in customers:
        print(f"\nNew customer: {customer['name']}")
        print(f"Customer wants: {customer['order']}")
        
        served_order = input("What will you serve? (coffee/tea/cake/crepes/brownie/sandwich/sugar cookie/fruit cup): ").strip().lower()
        
        while served_order not in orders:
            print("Invalid choice. Please choose the options from the menu.")
            served_order = input("What will you serve? (coffee/tea/cake/crepes/brownie/sandwich/sugar cookie/fruit cup): ").strip().lower()
        
        earned_coins, satisfaction = serve_customer(customer['order'], served_order)
        coins += earned_coins
        
        if satisfaction == "happy":
            print(f"You served the order correctly! You earned {earned_coins} coins.")
        else:
            print(f"You served the wrong order. You only earned {earned_coins} coins.")
        
        print(f"Total coins: {coins}")
        time.sleep(1)  # Pause for a moment for effect
    
    print("\nGame over!")
    print(f"Your final total is {coins} coins.")

if __name__ == "__main__":
    game()