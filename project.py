import requests
import datetime

class Farmer:
    def __init__(self, name, farm_location, contact_info):
        self.name = name
        self.farm_location = farm_location
        self.contact_info = contact_info
        self.crops = []
        self.irrigation_system = None

    def add_crop(self, crop):
        self.crops.append(crop)

    def remove_crop(self, crop_name):
        for crop in self.crops:
            if crop.name == crop_name:
                self.crops.remove(crop)
                break

    def display_crops(self):
        for crop in self.crops:
            print(crop)

    def set_irrigation_system(self, irrigation_system):
        self.irrigation_system = irrigation_system

    def irrigate_crop(self, crop_name):
        if self.irrigation_system is None:
            print(f"Farmer {self.name} does not have an irrigation system set up.")
        else:
            self.irrigation_system.irrigate_crop(crop_name)

    def estimate_yield(self, crop_name):
        for crop in self.crops:
            if crop.name == crop_name:
                estimated_yield = crop.estimate_yield()
                print(f"Estimated yield for {crop.name}: {estimated_yield}")
                break

    def get_weather_data(self, location):
        weather_data = {
            "temperature": "25°C",
            "precipitation": "0.2 inches",
            "humidity": "60%",
        }
        print(f"Weather data for {location}:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Precipitation: {weather_data['precipitation']}")
        print(f"Humidity: {weather_data['humidity']}")

    def check_pest_infestation(self, crop_name):
        for crop in self.crops:
            if crop.name == crop_name:
                if crop.pest_resistance == "High":
                    print("No signs of pests or diseases detected.")
                elif crop.pest_resistance == "Medium":
                    print("Some signs of pests or diseases detected.")
                    print("Recommendations: Apply organic pesticides and increase monitoring.")
                elif crop.pest_resistance == "Low":
                    print("Severe signs of pests or diseases detected.")
                    print("Recommendations: Apply chemical pesticides and quarantine the affected area.")
                break
        else:
            print(f"Crop {crop_name} not found.")


class Crop:
    def __init__(self, name, planting_date, harvest_date, water_requirements, pest_resistance):
        self.name = name
        self.planting_date = datetime.datetime.strptime(planting_date, "%Y-%m-%d")
        self.harvest_date = datetime.datetime.strptime(harvest_date, "%Y-%m-%d")
        self.water_requirements = water_requirements
        self.pest_resistance = pest_resistance

    def __str__(self):
        return f"Crop Name: {self.name}\nPlanting Date: {self.planting_date.strftime('%Y-%m-%d')}\nHarvest Date: {self.harvest_date.strftime('%Y-%m-%d')}\nWater Requirements: {self.water_requirements}\nPest Resistance: {self.pest_resistance}"

    def estimate_yield(self):
        days_to_harvest = (self.harvest_date - self.planting_date).days
        estimated_yield = days_to_harvest * 10
        return estimated_yield


class IrrigationSystem:
    def __init__(self, water_source, irrigation_type, coverage_area):
        self.water_source = water_source
        self.irrigation_type = irrigation_type
        self.coverage_area = coverage_area

    def irrigate_crop(self, crop_name):
        print(f"Irrigating {crop_name} using {self.irrigation_type} irrigation system from {self.water_source}")


def main():
    farmer1 = Farmer("John Smith", "123 Main Street", "johnsmith@email.com")

    while True:
        print("Welcome to the Farm Management System")
        print("What would you like to do?")
        print("1. Add a crop")
        print("2. Remove a crop")
        print("3. Display crops")
        print("4. Irrigate a crop")
        print("5. Estimate crop yield")
        print("6. Get weather data")
        print("7. Check for pests")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            crop_name = input("Enter crop name: ")
            planting_date = input("Enter planting date (YYYY-MM-DD): ")
            harvest_date = input("Enter harvest date (YYYY-MM-DD): ")
            water_requirements = input("Enter water requirements: ")
            pest_resistance = input("Enter pest resistance (High/Medium/Low): ")
            crop = Crop(crop_name, planting_date, harvest_date, water_requirements, pest_resistance)
            farmer1.add_crop(crop)

        elif choice == "2":
            crop_name = input("Enter crop name: ")
            farmer1.remove_crop(crop_name)

        elif choice == "3":
            farmer1.display_crops()

        elif choice == "4":
            crop_name = input("Enter crop name: ")
            farmer1.irrigate_crop(crop_name)

        elif choice == "5":
            crop_name = input("Enter crop name: ")
            farmer1.estimate_yield(crop_name)

        elif choice == "6":
            location = input("Enter location: ")
            farmer1.get_weather_data(location)

        elif choice == "7":
            crop_name = input("Enter crop name: ")
            farmer1.check_pest_infestation(crop_name)

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please try again.")

main()
