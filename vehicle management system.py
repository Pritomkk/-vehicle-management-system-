from tabulate import tabulate

class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        company= input("Enter vehicle Company name: ")
        model = input("Enter vehicle model: ")
        year = input("Enter vehicle year: ")
        vehicleIdentificationNumber= input("Enter vehicle Identification Number: ")
        license_plate = input("Enter vehicle license plate: ")
        purchase_date = input("Enter vehicle purchase date: ")

        vehicle = {
            "Company":  company,
            "model": model,
            "year": year,
            "vehicleIdentificationNumber": vehicleIdentificationNumber,
            "license_plate": license_plate,
            "purchase_date": purchase_date
        }
        
        self.vehicles.append(vehicle)
        print("Vehicle added successfully.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles added yet.")
        else:
            headers = ["Company Name", "Model", "Year", "vehicle Identification Number", "License Plate", "Purchase Date"]
            data = [[vehicle['Company'], 
                     vehicle['model'], 
                     vehicle['year'], 
                     vehicle['vehicleIdentificationNumber'], 
                     vehicle['license_plate'], 
                     vehicle['purchase_date']] for vehicle in self.vehicles]
            print(tabulate(data, headers=headers, tablefmt="grid"))

    def update_vehicle(self, vehicleIdentificationNumber):
        for vehicle in self.vehicles:
            if vehicle['vehicleIdentificationNumber'] == vehicleIdentificationNumber:
                print("Enter the details you want to update (press Enter to keep existing value):")
                updates = {
                    'Company': input(f"Company ({vehicle['Company']}): "),
                    'model': input(f"Model ({vehicle['model']}): "),
                    'year': input(f"Year ({vehicle['year']}): "),
                    'license_plate': input(f"License Plate ({vehicle['license_plate']}): "),
                    'purchase_date': input(f"Purchase Date ({vehicle['purchase_date']}): ")
                }

                for key, value in updates.items():
                    if value:
                        vehicle[key] = value

                print("Vehicle details updated successfully.")
                break
        else:
            print("Vehicle not found.")

    def delete_vehicle(self):
            vin = input("Enter VIN of the vehicle: ")
            vehicle_found = False
            for vehicle in self.vehicles:
                if vehicle['vehicleIdentificationNumber'] == vin:
                    vehicle_found = True
                    break

            if vehicle_found:
                for vehicle in self.vehicles:
                     if vehicle['vehicleIdentificationNumber'] == vin:
                        self.vehicles.remove(vehicle)
                        print("Vehicle deleted successfully.")
                        break
            else:
                print("Vehicle not found.")

class MaintenanceTracker:
    def __init__(self, vehicle_manager):
        self.maintenance_records = []
        self.vehicle_manager = vehicle_manager

    def record_maintenance(self):
        vin = input("Enter VIN of the vehicle: ")
        vehicle_found = False
        for vehicle in self.vehicle_manager.vehicles:
            if vehicle['vehicleIdentificationNumber'] == vin:
                vehicle_found = True
                break

        if vehicle_found:
            maintenance_type = input("Enter type of maintenance: ")
            date = input("Enter date of maintenance (YYYY-MM-DD): ")
            mileage = int(input("Enter mileage at the time of maintenance: "))
            details = input("Enter details of maintenance: ") 

            maintenance_record = {
                "vin": vin,
                "maintenance_type": maintenance_type,
                "date": date,
                "mileage": mileage,
                "details": details
            }
            self.maintenance_records.append(maintenance_record)
            print("Maintenance record added successfully.")
        else:
            print("Vehicle with VIN", vin, "does not exist. Please enter a valid VIN.")

    def display_maintenance_history(self, vin):
        print(f"Maintenance History for Vehicle with VIN: {vin}")
        found_records = False
        vehicle_records = []
        for record in self.maintenance_records:
            if record['vin'] == vin:
                vehicle_records.append([record['date'], record['maintenance_type'], record['mileage'], record['details']])
                found_records = True

        if found_records:
            headers = ["Date", "Maintenance Type", "Mileage", "Details"]
            print(tabulate(vehicle_records, headers=headers, tablefmt="grid"))
        else:
            print("No maintenance history found for this vehicle.")

class FuelExpenseTracker:
    def __init__(self,vehicle_manager):
        self.fuel_logs = []
        self.vehicle_manager = vehicle_manager

    def log_fuel_purchase(self):
        
        vin = input("Enter VIN of the vehicle: ")
        vehicle_found = False
        for vehicle in self.vehicle_manager.vehicles:
            if vehicle['vehicleIdentificationNumber'] == vin:
                vehicle_found = True
                break
       
        if vehicle_found:
            fuel_type = input("Enter fuel type: ")
            quantity = float(input("Enter quantity of fuel : "))
            price_per_unit = float(input("Enter price per unit of fuel: "))
            odometer_reading = int(input("Enter odometer reading at the time of purchase: "))

            fuel_log = {
                "vin": vin,
                "fuel_type": fuel_type,
                "quantity": quantity,
                "price_per_unit": price_per_unit,
                "total_cost": quantity*price_per_unit,
                "odometer_reading": odometer_reading
            }
            self.fuel_logs.append(fuel_log)
            print("Fuel purchase logged successfully.")
        
        else:
            print("Vehicle with VIN", vin, "does not exist. Please enter a valid VIN.")
      
    def display_fuel_logs_and_Cost(self):
        if not self.fuel_logs:
            print("No fuel purchase logs available.")
        else:
            headers = ["VIN", "Fuel Type", "Quantity", "Price per Unit", "Total Cost", "Odometer Reading"]
            data = [[log['vin'], log['fuel_type'], 
                     log['quantity'], log['price_per_unit'], 
                     log['total_cost'], log['odometer_reading']] for log in self.fuel_logs]
            print(tabulate(data, headers=headers, tablefmt="grid"))

    def calculate_fuel_efficiency(self):
        vin = input("Enter VIN of the vehicle: ")
        vehicle_found = False
        for vehicle in self.vehicle_manager.vehicles:
            if vehicle['vehicleIdentificationNumber'] == vin:
                vehicle_found = True
                break
        
        if vehicle_found:
            total_distance = 0
            total_fuel = 0

            for log in self.fuel_logs:
                if log['vin'] == vin:
                    total_distance += log['odometer_reading']
                    total_fuel += log['quantity']

            if total_fuel == 0:
                print("No fuel logs found for this vehicle.")
                return

            fuel_efficiency = total_distance / total_fuel
            print(f"Fuel efficiency for Vehicle with VIN {vin}: {fuel_efficiency} miles per gallon (MPG)")
        
        else:
            print("Vehicle with VIN", vin, "does not exist. Please enter a valid VIN.")

class ServiceReminder:
    def __init__(self,vehicle_manager):
        self.reminders = []
        self.vehicle_manager = vehicle_manager

    def set_custom_reminder(self):
        vin = input("Enter VIN of the vehicle: ")
        vehicle_found = False
        for vehicle in self.vehicle_manager.vehicles:
            if vehicle['vehicleIdentificationNumber'] == vin:
                vehicle_found = True
                break
 
        if vehicle_found:
            frequency = input("Enter reminder frequency :")
            notification= input("Enter notification preferences : ")
            reminder = {
                "vin": vin,
                "frequency": frequency,
                "notification_preferences": notification
            }
            self.reminders.append(reminder)
            print("Custom reminder set successfully.")

        else:
            print("Vehicle with VIN", vin, "does not exist. Please enter a valid VIN.")

    def show_custom_reminders(self):
        if not self.reminders:
            print("No custom reminders set.")
        else:
            print("Custom Reminders:")
            for idx, reminder in enumerate(self.reminders, start=1):
                print(f"Reminder {idx}:")
                print(f"VIN: {reminder['vin']}")
                print(f"Frequency: {reminder['frequency']} months")
                print(f"Notification Preferences: {reminder['notification_preferences']}")
                print() 

class UserAuthentication:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(":")
                    self.users[username] = password
        except FileNotFoundError:
            pass

    def save_users(self):
        with open("users.txt", "w") as file:
            for username, password in self.users.items():
                file.write(f"{username}:{password}\n")

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = password
            self.save_users()
            print("User registered successfully.")

    def login(self):
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username not in self.users:
                print("User not found. Please register first.")
            elif self.users[username] != password:
                print("Incorrect password. Please try again.")
            else:
                print("Login successful. Welcome,", username)
                break  


def main():
    auth = UserAuthentication()
    print("***************Welcome to Vehicle Management System******************")
    print("Select an option:")
    print("1. Register a new user")
    print("2. Login to the system")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("\nRegister a new user:")
        auth.register_user()
    elif choice == "2":
        print("\nLogin to the system:")
        auth.login()
    elif choice == "3":
        print("Exiting program.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    if auth.users:
        vehicle_manager = VehicleManager()
        maintenance_tracker = MaintenanceTracker(vehicle_manager)
        fuel_expense_tracker = FuelExpenseTracker(vehicle_manager)
        service_reminder = ServiceReminder(vehicle_manager)

        while True:
            print("\nMenu:")
            print("1. Add Vehicle")
            print("2. Display Vehicles")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("5. Record Maintenance")
            print("6. Display Maintenance History")
            print("7. Log Fuel Purchase")
            print("8. Display fuel logs and cost")
            print("9. Calculate Fuel Efficiency")
            print("10. Set Custom Reminder")
            print("11. Show Custom Reminders")
            print("12. Exit")
            choice = input("Enter your choice: ")

            options = {
                "1": vehicle_manager.add_vehicle,
                "2": vehicle_manager.display_vehicles,
                "3": lambda: vehicle_manager.update_vehicle(input("Enter VIN of the vehicle to update: ")),
                "4": vehicle_manager.delete_vehicle,
                "5": maintenance_tracker.record_maintenance,
                "6": lambda: maintenance_tracker.display_maintenance_history(input("Enter VIN of the vehicle: ")),
                "7": fuel_expense_tracker.log_fuel_purchase,
                "8": fuel_expense_tracker.display_fuel_logs_and_Cost,
                "9": fuel_expense_tracker.calculate_fuel_efficiency,
                "10": service_reminder.set_custom_reminder,
                "11": service_reminder.show_custom_reminders,
                "12": lambda: (print("Exiting program."), exit(0))
            }

            selected_option = options.get(choice)
            if selected_option:
                selected_option()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

