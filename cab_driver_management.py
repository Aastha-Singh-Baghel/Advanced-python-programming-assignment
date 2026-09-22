import json

FILE = "drivers.json"


# Load drivers from JSON file
def load_drivers():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Save drivers to JSON file
def save_drivers(drivers):
    with open(FILE, "w") as f:
        json.dump(drivers, f, indent=4)


# 1. Add driver
def add_driver():
    drivers = load_drivers()

    driver = {
        "driver_id": input("Enter Driver ID: "),
        "name": input("Enter Driver Name: "),
        "mobile": input("Enter Mobile Number: "),
        "cab_number": input("Enter Cab Number: "),
        "cab_type": input("Enter Cab Type: "),
        "experience": int(input("Enter Experience (years): ")),
        "rating": float(input("Enter Rating: ")),
        "availability": input("Enter Availability (Yes/No): ")
    }

    drivers.append(driver)
    save_drivers(drivers)

    print("Driver added successfully!")


# 2. Display all drivers
def display_all():
    drivers = load_drivers()

    if len(drivers) == 0:
        print("No drivers found.")
        return

    for driver in drivers:
        print("\nDriver ID:", driver["driver_id"])
        print("Name:", driver["name"])
        print("Mobile:", driver["mobile"])
        print("Cab Number:", driver["cab_number"])
        print("Cab Type:", driver["cab_type"])
        print("Experience:", driver["experience"], "years")
        print("Rating:", driver["rating"])
        print("Availability:", driver["availability"])


# 3. Search driver by ID
def search_driver():
    drivers = load_drivers()

    id = input("Enter Driver ID to search: ")

    for driver in drivers:
        if driver["driver_id"] == id:
            print("\nDriver Found")
            print("Driver ID:", driver["driver_id"])
            print("Name:", driver["name"])
            print("Mobile:", driver["mobile"])
            print("Cab Number:", driver["cab_number"])
            print("Cab Type:", driver["cab_type"])
            print("Experience:", driver["experience"])
            print("Rating:", driver["rating"])
            print("Availability:", driver["availability"])
            return

    print("Driver not found.")


# 4. Update driver availability
def update_availability():
    drivers = load_drivers()

    id = input("Enter Driver ID: ")

    for driver in drivers:
        if driver["driver_id"] == id:
            driver["availability"] = input("Enter new availability (Yes/No): ")
            save_drivers(drivers)
            print("Availability updated successfully!")
            return

    print("Driver not found.")


# 5. Search drivers with rating above given value
def search_by_rating():
    drivers = load_drivers()

    rating = float(input("Enter rating value: "))

    found = False

    for driver in drivers:
        if driver["rating"] > rating:
            print("\nDriver ID:", driver["driver_id"])
            print("Name:", driver["name"])
            print("Rating:", driver["rating"])
            found = True

    if found == False:
        print("No drivers found.")


# 6. Delete driver
def delete_driver():
    drivers = load_drivers()

    id = input("Enter Driver ID to delete: ")

    for driver in drivers:
        if driver["driver_id"] == id:
            drivers.remove(driver)
            save_drivers(drivers)
            print("Driver deleted successfully!")
            return

    print("Driver not found.")


# 7. Display available drivers
def display_available():
    drivers = load_drivers()

    found = False

    for driver in drivers:
        if driver["availability"].lower() == "yes":
            print("\nDriver ID:", driver["driver_id"])
            print("Name:", driver["name"])
            print("Cab Number:", driver["cab_number"])
            print("Cab Type:", driver["cab_type"])
            print("Rating:", driver["rating"])
            found = True

    if found == False:
        print("No available drivers.")


# Main menu
while True:
    print("\n===== CAB DRIVER MANAGEMENT SYSTEM =====")
    print("1. Add Driver")
    print("2. Display All Drivers")
    print("3. Search Driver by ID")
    print("4. Update Driver Availability")
    print("5. Search Drivers by Rating")
    print("6. Delete Driver")
    print("7. Display Available Drivers")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_driver()

    elif choice == "2":
        display_all()

    elif choice == "3":
        search_driver()

    elif choice == "4":
        update_availability()

    elif choice == "5":
        search_by_rating()

    elif choice == "6":
        delete_driver()

    elif choice == "7":
        display_available()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")