class Vehicle:
    """
    A super class to store the general type of a vehicle.
    """
    def __init__(self, vehicle_type):
        """
        Initializes the Vehicle class.
        
        Args:
            vehicle_type (str): The type of vehicle (e.g., car, truck, plane).
        """
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    """
    A class representing an automobile, inheriting from Vehicle.
    It stores detailed information about a car.
    """
    def __init__(self, year, make, model, doors, roof):
        """
        Initializes the Automobile class.
        
        Args:
            year (str or int): The manufacturing year.
            make (str): The manufacturer (e.g., Toyota).
            model (str): The model name (e.g., Corolla).
            doors (str or int): The number of doors (e.g., 2 or 4).
            roof (str): The type of roof (e.g., solid or sun roof).
        """
        # Call the super class's (Vehicle's) __init__ method
        # We hardcode "car" as per the requirements.
        super().__init__("car")
        
        # Assign the specific attributes for an Automobile
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        """
        Prints the collected vehicle information in a readable format.
        """
        print("\n--- Vehicle Details ---")
        print(f"  Vehicle type: {self.vehicle_type}")
        print(f"  Year: {self.year}")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}")
        print("-----------------------")

def main():
    """
    Main function to run the application.
    It prompts the user for car details, creates an Automobile object,
    and then displays the entered information.
    """
    print("Please enter the details for your car.")
    
    # Get user input for each attribute
    try:
        year = input("Enter the year: ")
        make = input("Enter the make: ")
        model = input("Enter the model: ")
        doors = input("Enter the number of doors (e.g., 2 or 4): ")
        roof = input("Enter the type of roof (e.g., solid or sun roof): ")
        
        # Create an instance of the Automobile class
        my_car = Automobile(year, make, model, doors, roof)
        
        # Call the method to display the car's information
        my_car.display_info()
        
    except KeyboardInterrupt:
        print("\n\nInput cancelled. Exiting.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Standard Python entry point
if __name__ == "__main__":
    main()