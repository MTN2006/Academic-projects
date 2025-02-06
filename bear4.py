def read_inventory(filename):
    inventory = {}  # initialize empty dictionary

    with open(filename, "r") as file:  # open file
        for line in file:
            parts = line.strip().split(',')  # split the data into sections

            item_name = parts[0] 
            cpu = float(parts[1])
            uin = int(parts[2])

            inventory[item_name] = [cpu, uin]  # store extracted data in a dictionary
    return inventory


def display_inventory(inventory):
    for item_name, details in inventory.items():
        cpu = details[0]  # cost per unit
        uin = details[1]  # units in stock
        print(f'{item_name} ${cpu:.2f} Qty:{uin}')


def add_item(inventory):
    item_name = input('Enter item: ')
    if item_name in inventory:
        print(f'{item_name} already exists')
    else: 
        cpu_input = input('Enter cost: ')
        try:
            cpu = float(cpu_input)
        except ValueError:
            print('Invalid cost')
            return
        
        uin_input = input('Enter availability: ')
        try:
            uin = int(uin_input)
        except ValueError:
            print('Invalid number of units')
            return
        
        inventory[item_name] = [cpu, uin]
        print(f'Added {item_name}')


def delete_item(inventory):
    item_name = input('Enter item: ')
    if item_name in inventory:
        del inventory[item_name]
        print(f'Deleted {item_name}')
    else:
        print(f'{item_name} not found')


def update_cost(inventory):
    item_name = input('Enter item: ')
    if item_name in inventory:
        try:
            percent = float(input('Enter percentage increase: '))
            if percent < 0:
                print('Percent cannot be negative')
                return
        except ValueError:
            print('Invalid percentage')
            return
        
        # Get the current cost of the item
        current_cost = inventory[item_name][0]
        
        # Calculate the new cost
        new_cost = current_cost * (1 + percent / 100)
        
        # Update the cost in the inventory dictionary without rounding
        inventory[item_name][0] = new_cost
        
        print(f'Updated {item_name}')
    else:
        print(f'{item_name} not found')


def above_average_cost(inventory):
    total_cost = 0
    num_items = 0

    for item_name, details in inventory.items():
        total_cost += details[0]
        num_items += 1

    if num_items > 0:
        avg_cost = total_cost / num_items
    else:
        avg_cost = 0

    print(f"Average cost: {avg_cost:.2f}")

    # Step 4: Find and display items with cost greater than the average
    print("Items above average cost:")
    for item_name, details in inventory.items():
        if details[0] > avg_cost:  # If cost per unit is greater than the average
            print(f"{item_name} ${details[0]:.2f}")


def sell_item(inventory):
    item_name= input('Enter item: ')
    if item_name not in inventory:
        print(f'{item_name} not found')
        return
    
    a_qty= inventory[item_name][1]
    if a_qty==0:
        print(f'{item_name} is not available')
        return
    try:
        units_to_sell = int(input(f'Enter quantity: '))
    except ValueError:
        print("Invalid input, please enter an integer.")
        return

    if units_to_sell > a_qty:
        units_to_sell = a_qty  # Sell the entire stock if more than available

    total_cost = units_to_sell * inventory[item_name][0]
    remaining_qty = a_qty - units_to_sell
    inventory[item_name][1] = remaining_qty  # Update remaining stock

    print(f'{units_to_sell} out of {a_qty} sold for ${total_cost:.2f}, with {remaining_qty} units remaining ')


def out_of_stock(inventory):
    out_of_stock_items = [item for item, details in inventory.items() if details[1] == 0]

    if out_of_stock_items:
        print("OUT OF STOCK:")
        for item in out_of_stock_items:
            print(f'{item}')
    else:
        print('OUT OF STOCK:')
        print("All items are in stock.")


def main():
    # Prompt the user to enter the filename of the inventory file
    filename = input("Enter the file: ")

    # Read the inventory from the file
    inventory = read_inventory(filename)

    # Check if the inventory is empty (in case of an error with reading the file)
    if not inventory:
        print("No inventory data found.")
        return  # Exit the program if the inventory is empty

    # Menu loop to interact with the user
    while True:
        # Display menu options
        print("\nMENU:")
        print("1. Display inventory")
        print("2. Exit")
        print('3. Add item')
        print('4. Delete item')
        print('5. Update cost')
        print('6. Items above average cost')
        print('7. Sell item')
        print('8. Out of stock')

        # Prompt the user for their choice
        choice = input("Enter choice: ")

        if choice == '1':
            # Display the inventory
            print('INVENTORY:')
            display_inventory(inventory)
        elif choice == '2':
            # Exit the program
            print("Goodbye")
            break  # Exit the while loop and terminate the program
        elif choice == '3':
            add_item(inventory)
        elif choice == '4':
            delete_item(inventory)
        elif choice == '5':
            # Update the cost of an item
            update_cost(inventory)
        elif choice == '6':
            # Display items above the average cost
            above_average_cost(inventory)
        elif choice == '7':
            # Sell item
            sell_item(inventory)
        elif choice == '8':
            # Display out of stock items
            out_of_stock(inventory)
        else:
            # Handle invalid input
            print("Invalid choice")

if __name__ == "__main__":
    main()
