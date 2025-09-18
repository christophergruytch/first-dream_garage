# wish to create a small terminal program where you can create
# a "dream garage" and write it to a file, then retrieve that
# data and read it out and delete garages and so on, I also 
# want to create a file that has all the possible cars
# someone may want, but are not necessarily in one of their 
# garages.


import json
import time


def main_menu(username):
    print()
    print(f"Hello {username}")
    print("Would you like to edit your car list or your garages?")
    print("1. Edit My Car List")
    print("2. Edit My Garages")
    print()

def list_menu():
    print("\nWelcome To Your Car List Menu")
    print("What would you like to do?")
    print("1. View My Car List")
    print("2. Add A Car To My List")
    print("3. Remove A Car From My List")
    print("4. Quit\n")

    option = int(input("What would you like to do? (1-4): "))

    if option == 1:
        view_car_list()
    elif option == 2:
        add_car_list()
    elif option == 3:
        delete_car_list()
    elif option == 4:
        quit()
    else:
        print("Not a valid entry")

def garage_menu():
    print("\nWelcome To Your Garage Menu")
    print("What would you like to do?")
    print("1. View A Garage")
    print("2. Create A New Garage")
    print("3. Delete A Garage")
    print("4. Edit An Existing Garage")
    print("5. Quit\n")

    print("I'm sorry, this function is still being created.")
    print("As of right now, only editing the car list is doable.\n")
    time.sleep(3)



# def hello(username):
#     print()
#     print(f"Hello {username}, what would you like to do today?")
#     print("1. Create A New Garage")
#     print("2. View A Garage Or Your Car List")
#     print("3. Update An Existing Garage")
#     print("4. Delete A Garage Or A Car From Your List")
#     print("5. Add A Car To Your List")
#     print("6. Quit / Exit the Program")
#     print()

    
def create_garage():
    print("You are creating")

def view_car_list():
    # print("You are viewing")

    try:
        with open("car_holder.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"cars": []}
    
    print()
    print("The cars in your car holder include: ")
    for car in data["cars"]:
        print(car)
    print()

def update_garage():
    print("You are updating")


def delete_car_list():
    """Remove a car name from car_holder.json with confirmation."""
    # Load existing data from car_holder.json
    try:
        with open("car_holder.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No cars found in car_holder.json!")
        return

    # Check if there are any cars to delete
    if not data.get("cars"):
        print("No cars available to delete!")
        return

    # Display cars with indices
    print("\nYour cars:")
    for index, car in enumerate(data["cars"]):
        print(f"{index}: {car}\n")

    # Get user input for the car to delete
    try:
        car_index = int(input("Enter the index of the car to delete: ").strip())
        if 0 <= car_index < len(data["cars"]):
            car_name = data["cars"][car_index]  # Get the car name for confirmation
            # Ask for confirmation
            are_you_sure = input(f"Are you sure you want to delete '{car_name}'? (y/n): ").strip().lower()
            if are_you_sure == 'y' or are_you_sure == "yes":
                removed_car = data["cars"].pop(car_index)  # Remove the car
                # Save updated data back to car_holder.json
                try:
                    with open("car_holder.json", "w") as file:
                        json.dump(data, file, indent=4)
                    print(f"Deleted '{removed_car}' from car_holder.json!")
                except Exception as e:
                    print(f"Error saving to car_holder.json: {e}")
            else:
                print(f"Deletion of '{car_name}' canceled.")
        else:
            print("Invalid index! Please choose a number from the list.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    print()
    print("The cars in your car holder now include: ")
    for car in data["cars"]:
        print(car)
    print()

def add_car_list():
    # print("You are adding a car to your list")

    try:
        with open("car_holder.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"cars": []}

    car_name = input("Please enter the car you would like to add: ").strip()

    data["cars"].append(car_name)

    try:
        with open("car_holder.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"Added '{car_name}' to car_holder.json!")
    except Exception as e:
        print(f"Error saving to car_holder.json: {e}")

    

def quit():
    print("You are quiting")


if __name__ == '__main__':

    keep_going = True

    while keep_going:

        username = "Chris"

        main_menu(username)

        menu = int(input("Please select a menu (1-2): "))

        if menu == 1:
            list_menu()
        elif menu == 2:
            garage_menu()

        # hello("Chris")
        
        # number = int(input("Please enter which one (1-6): "))

        # if number == 1:
        #     create()
        # elif number == 2:
        #     view()
        # elif number == 3:
        #     update()
        # elif number == 4:
        #     delete()
        # elif number == 5:
        #     add()
        # elif number == 6:
        #     quit()
        #     sure = input("Are you certain? (y/n): ").lower().strip()
        #     if sure == 'n' or sure == 'no':
        #         continue
        #     else:
        #         break

        stop = input("Would you like to do something else? (y/n): ").strip().lower()
    
        while stop != "n" or stop == "no":
            if stop == "y" or stop == "yes":
                break
            elif stop == "n" or stop == "no":
                break
            print(f"'{stop}' is not a valid entry.")
            stop = input("Would you like to do something else? (y/n): ").strip().lower()
        if stop == "n" or stop == "no":
            keep_going = False
        

