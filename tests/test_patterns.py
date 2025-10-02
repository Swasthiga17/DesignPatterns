import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from behavioral.observer_stock_market import Stock, MobileApp
from behavioral.strategy_payment import PaymentProcessor, CreditCardPayment
from creational.factory_vehicles import VehicleFactory, VehicleType
from creational.singleton_config import ConfigurationManager
from structural.decorator_coffee import SimpleCoffee, MilkDecorator
import tempfile

def test_observer():
    stock = Stock("TEST", 100)
    app = MobileApp("TestApp")
    stock.add_observer(app)
    
    # Test with file output
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        stock.set_price(110, f)
        f.flush()
        with open(f.name, 'r') as result_file:
            content = result_file.read()
            assert "StockTracker Pro" in content
    os.unlink(f.name)

def test_strategy():
    processor = PaymentProcessor()
    credit_card = CreditCardPayment("1111222233334444", "12/25", "123")
    processor.set_payment_strategy(credit_card)
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        processor.execute_payment(50.0, f)
        f.flush()
        with open(f.name, 'r') as result_file:
            content = result_file.read()
            assert "credit card" in content.lower()
    os.unlink(f.name)

def test_factory():
    car = VehicleFactory.create_vehicle(VehicleType.CAR, "Test Car")
    assert car.__class__.__name__ == "Car"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        car.start_engine(f)
        f.flush()
        with open(f.name, 'r') as result_file:
            content = result_file.read()
            assert "Engine started" in content
    os.unlink(f.name)

def test_singleton():
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    assert config1 is config2
    
    # Test configuration persistence
    config1.set("test_key", "test_value")
    assert config2.get("test_key") == "test_value"

def test_decorator():
    coffee = SimpleCoffee()
    coffee_with_milk = MilkDecorator(coffee)
    assert coffee_with_milk.get_cost() > coffee.get_cost()
    assert "milk" in coffee_with_milk.get_description()

def run_all_tests():
    print("Running tests...")
    test_observer()
    test_strategy()
    test_factory()
    test_singleton()
    test_decorator()
    print("All tests passed! ✅")

if __name__ == "__main__":
    run_all_tests()