menu = {
    "Burrito": {
        "Chicken": 4.49,
        "Beef": 5.49,
        "Vegetarian": 3.99
    },
    "Rice Bowl": {
        "Teriyaki Chicken": 9.99,
        "Sweet and Sour Pork": 8.99
    },
    "Sushi": {
        "California Roll": 7.49,
        "Spicy Tuna Roll": 8.49
    },
    "Noodles": {
        "Pad Thai": 6.99,
        "Lo Mein": 7.99,
        "Mee Goreng": 8.99
    },
    "Pizza": {
        "Cheese": 8.99,
        "Pepperoni": 10.99,
        "Vegetarian": 9.99
    },
    "Burger": {
        "Chicken": 7.49,
        "Beef": 8.49
    }
}
def process_order_input(menu_selection):
    """
    Validates and processes the customer's menu selection input.

    Parameters:
    menu_selection (str): The customer's menu selection input.

    Returns:
    int: The menu selection converted to an integer if valid.

    Raises:
    ValueError: If the menu selection is not a valid number.
    """
    # Check if the customer left menu_selecton empty
    if not menu_selection:
        raise ValueError("Sorry, menu selection cannot be empty.")
        # return order

     # Check if the customer entered a number    
    if not menu_selection.isdigit():
        raise ValueError("Sorry, menu selection must be a number")
        # return order
    # Convert the menu selection to an integer
    num = int(menu_selection)
    
    # Check if the customer entered a number between 1 and the total number of menu items
    if num < 1 or num > len(get_menu_items_dict(menu)):
        raise ValueError(f"Sorry, menu selection must be between 1 and {len(get_menu_items_dict(menu))}")
    
    return num
    

def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []
    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)
    order_total = 0.0
   
    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    # TODO: Create a continuous while loop so customers can order multiple items
    ordering = True
    while ordering:
        # TODO: Ask the customer what they want to order
        print("What would you like to order?")
       
        # Create a variable for the menu item number
        i = 1

        # Print the menu header
        print_menu_heading()

        # Loop through the menu dictionary
        for food_category, options in menu.items():
               for meal, price in options.items():
                print_menu_line(i, food_category, meal, price)
                i += 1
        # Ask customer to input menu item number
        try:
            menu_selection = input("\nPlease enter the number of the item you want to order:")
            num = process_order_input(menu_selection)
            print(f"Valid menu selection: {num}")
        except ValueError as e:
            print(e)
            continue
        # TODO: Update the order list using the update_order function        
        # TODO: Send the order list, menu selection, and menu items as arguments
        order = update_order(order, str(num), menu_items)
        # print("Order updated:", order)
        print("Order updated.")

        keep_ordering = input("\nWould you like to order anything else? (Enter 'n'/'N' to finish and 'y/'Y' to continue:")
    
        if keep_ordering.lower() == 'n':
            print("Ordering fininshed")
            print("\nThank you for your order!")
            ordering = False
       
            # TODO: The total price for each item should multiply the price by quantity
            prices_list = [item["Price"] * item["Quantity"] for item in order]

            # TODO: Create an order_total from the prices list using sum()
            # TODO: Round the prices to 2 decimal places.
            order_total = round(sum(prices_list), 2)

               # Create the receipt
    receipt = [{"Item name": item["Item name"], "Price": item["Price"], "Quantity":item["Quantity"]} for item in order]
   

    # TODO: Return the order list and the order total
    return order, order_total

def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    num = None # Initialize num outside thr try block

    try :
        num = int(menu_selection)

        if num in menu_items:
            item_name = menu_items[num]["Item name"]

            quantity_input = input(f"How many {item_name}s would you like to order?")

            try:
                quantity = int(quantity_input)
            except ValueError:
                print("Invalid quantity. Setting quantity to 1")
                quantity = 1
            order.append({
                "Item name": item_name,
                "Price": menu_items[num]["Price"],
                "Quantity": quantity
            })
        else:
            print(f"Menu selection {num} is not a valid menu option.")
    except ValueError:
        print(f"'{menu_selection}' is not a valid menu selection.")
    return order
    

def print_itemized_receipt(receipt, total_price):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
   
    # TODO: Loop through the items in the customer's receipt
    for item in receipt:
        # Store the dictionary items as variables
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # TODO: Print the receipt line using the print_receipt_line function
        print_receipt_line(item_name, price, quantity)
        # TODO: Send the item name, price, and quantity as separate arguments
        

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt, total_price) # added total_price

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)



