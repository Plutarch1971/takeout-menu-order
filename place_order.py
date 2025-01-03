def place_order(menu):
    # 1. Initialize order list and get menu items
    order = []
    menu_items = get_menu_items_dict(menu)
    
    # 2. Print welcome message
    print("Welcome to the Generic Take Out Restaurant.")
    
    # 3. Start continuous ordering loop
    ordering = True
    while ordering:
        print("What would you like to order?")
        
        # 4. Print menu header
        print_menu_heading()
        
        # 5. Display menu items with numbers
        i = 1
        for food_category, options in menu.items():
            for meal, price in options.items():
                print_menu_line(i, food_category, meal, price)
                i += 1
        
        # 6. Get customer's menu selection
        menu_selection = input("\nPlease enter the number of the item you want to order: ")
        
        # 7. Update order list with selected item
        order = update_order(order, menu_selection, menu_items)
        
        # 8. Ask if customer wants to continue
        keep_ordering = input("\nWould you like to order anything else? (Enter 'n' to finish): ")
        
        # 9. Check if customer wants to quit
        if keep_ordering.lower() == 'n':
            print("\nThank you for your order!")
            
            # 10. Calculate total price using list comprehension
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            
            # 11. Sum up total price
            order_total = round(sum(prices_list), 2)
            
            # 12. Exit ordering loop
            ordering = False
    
    # 13. Return final order and total
    return order, order_total