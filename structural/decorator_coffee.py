from abc import ABC, abstractmethod
import os

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.50
    
    def get_description(self) -> str:
        return "Simple coffee"

# Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def get_cost(self) -> float:
        return self._coffee.get_cost()
    
    def get_description(self) -> str:
        return self._coffee.get_description()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.25
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", whipped cream"

class CaramelDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.00
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", caramel"

class ChocolateDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.80
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", chocolate"

def demo_decorator(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/decorator_coffee.txt", "w") as f:
        f.write("=== Decorator Pattern: Coffee Shop ===\n\n")
        
        # Simple coffee
        coffee = SimpleCoffee()
        f.write(f"1. {coffee.get_description()} - ${coffee.get_cost():.2f}\n")
        
        # Coffee with milk and sugar
        coffee_with_milk_sugar = SugarDecorator(MilkDecorator(SimpleCoffee()))
        f.write(f"2. {coffee_with_milk_sugar.get_description()} - ${coffee_with_milk_sugar.get_cost():.2f}\n")
        
        # Fancy coffee with everything
        fancy_coffee = CaramelDecorator(
            WhippedCreamDecorator(
                ChocolateDecorator(
                    MilkDecorator(SimpleCoffee())
                )
            )
        )
        f.write(f"3. {fancy_coffee.get_description()} - ${fancy_coffee.get_cost():.2f}\n\n")
        
        # Build custom coffee step by step
        f.write("Building custom coffee step by step:\n")
        my_coffee = SimpleCoffee()
        f.write(f"Base: {my_coffee.get_description()} - ${my_coffee.get_cost():.2f}\n")
        
        my_coffee = MilkDecorator(my_coffee)
        f.write(f"After milk: {my_coffee.get_description()} - ${my_coffee.get_cost():.2f}\n")
        
        my_coffee = ChocolateDecorator(my_coffee)
        f.write(f"After chocolate: {my_coffee.get_description()} - ${my_coffee.get_cost():.2f}\n")
        
        my_coffee = WhippedCreamDecorator(my_coffee)
        f.write(f"Final: {my_coffee.get_description()} - ${my_coffee.get_cost():.2f}\n\n")
        
        f.write("Decorator pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_decorator()