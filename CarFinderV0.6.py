#I've been using Functions this whole time without realizing we weren't supposed to, oops

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'authorized_vehicles.txt')

def load_vehicles():
    with open(FILE_PATH, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def save_vehicles(vehicles):
    with open(FILE_PATH, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def print_vehicles(vehicles):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)
    print()

def search_vehicle(vehicles):
    print("\nPlease Enter the full Vehicle name:")
    query = input().strip()
    if query in vehicles:
        print(f"\n{query} is an authorized vehicle\n")
    else:
        print(f"\n{query} is not an authorized vehicle, if you received this in error please check the spelling and try again\n")

def add_vehicle(vehicles):
    print("\nPlease Enter the full Vehicle name you would like to add:")
    new_vehicle = input().strip()
    if new_vehicle in vehicles:
        print(f'\n"{new_vehicle}" is already in the authorized list.\n')
    else:
        vehicles.append(new_vehicle)
        save_vehicles(vehicles)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle\n')

def delete_vehicle(vehicles):
    print("\nPlease Enter the full Vehicle name you would like to REMOVE:")
    vehicle_to_remove = input().strip()
    if vehicle_to_remove in vehicles:
        print(f'\nAre you sure you want to remove "{vehicle_to_remove}" from the Authorized Vehicles List?')
        confirmation = input().strip().lower()
        if confirmation == "yes":
            vehicles.remove(vehicle_to_remove)
            save_vehicles(vehicles)
            print(f'\nYou have REMOVED "{vehicle_to_remove}" as an authorized vehicle\n')
        else:
            print("\nVehicle not removed.\n")
    else:
        print(f'\n"{vehicle_to_remove}" is not currently on the Authorized Vehicles List.\n')

def main():
    while True:
        vehicles = load_vehicles()
        print_menu()
        user_input = input()

        if user_input == "1":
            print_vehicles(vehicles)
        elif user_input == "2":
            search_vehicle(vehicles)
        elif user_input == "3":
            add_vehicle(vehicles)
        elif user_input == "4":
            delete_vehicle(vehicles)
        elif user_input == "5":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!\n(Press Enter to exit)")
            input("\n")
            break
        else:
            print("\nInvalid input. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
        main()
