from abc import ABC, abstractmethod
from enum import Enum
import os

class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self, output_file=None):
        pass
    
    @abstractmethod
    def stop_engine(self, output_file=None):
        pass

class Car(Vehicle):
    def __init__(self, model: str):
        self.model = model
    
    def start_engine(self, output_file=None):
        message = f"Car {self.model}: Engine started quietly"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def stop_engine(self, output_file=None):
        message = f"Car {self.model}: Engine stopped"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def __str__(self):
        return f"Car: {self.model}"

class Motorcycle(Vehicle):
    def __init__(self, model: str):
        self.model = model
    
    def start_engine(self, output_file=None):
        message = f"Motorcycle {self.model}: Engine ROARS to life!"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def stop_engine(self, output_file=None):
        message = f"Motorcycle {self.model}: Engine shut down"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def __str__(self):
        return f"Motorcycle: {self.model}"

class Truck(Vehicle):
    def __init__(self, model: str):
        self.model = model
    
    def start_engine(self, output_file=None):
        message = f"Truck {self.model}: Diesel engine rumbles powerfully"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def stop_engine(self, output_file=None):
        message = f"Truck {self.model}: Heavy engine stopped"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
    
    def __str__(self):
        return f"Truck: {self.model}"

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType, model: str) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car(model)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(model)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(model)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

def demo_factory(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/factory_vehicles.txt", "w") as f:
        f.write("=== Factory Pattern: Vehicle Manufacturing ===\n\n")
        factory = VehicleFactory()
        
        vehicles = [
            factory.create_vehicle(VehicleType.CAR, "Toyota Camry"),
            factory.create_vehicle(VehicleType.MOTORCYCLE, "Harley Davidson"),
            factory.create_vehicle(VehicleType.TRUCK, "Ford F-150")
        ]
        
        for i, vehicle in enumerate(vehicles, 1):
            f.write(f"Vehicle {i}: {vehicle}\n")
            f.write("Starting engine: ")
            vehicle.start_engine(f)
            f.write("Stopping engine: ")
            vehicle.stop_engine(f)
            f.write("\n")
        
        f.write("Factory pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_factory()