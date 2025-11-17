"""
Name: Mohamad Suhail Mohamad Solim
File Name: car_details_app.py
Description: 
This program uses object-oriented programming (OOP) to collect and display
information about a car. It defines a superclass 'Vehicle' and a
subclass 'Automobile' which inherits from 'Vehicle'. The program
prompts the user to enter details for a car, stores this data in an
'Automobile' object, and then prints the collected details in a
formatted way.

Key Variables/Attributes:
    Vehicle.vehicle_type (str): Stores the general type of the vehicle 
                                (e.g., "car", "truck").
    Automobile.year (str/int): The manufacturing year of the automobile.
    Automobile.make (str): The manufacturer of the automobile.
    Automobile.model (str): The model of the automobile.
    Automobile.doors (str/int): The number of doors on the automobile.
    Automobile.roof (str): The type of roof on the automobile.

Design Notes:
- This program is designed to be efficient, using simple classes and
  direct user input/output. It avoids unnecessary data structures
  or complex operations to minimize memory and processor usage.
- Error handling is included in the main function to gracefully
  manage unexpected input or interruptions.
"""

class Vehicle:
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
