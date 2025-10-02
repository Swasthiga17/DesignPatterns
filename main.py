from behavioral.observer_stock_market import demo_observer
from behavioral.strategy_payment import demo_strategy
from creational.factory_vehicles import demo_factory
from creational.singleton_config import demo_singleton
from structural.adapter_media import demo_adapter
from structural.decorator_coffee import demo_decorator
import os
import datetime

def main():
    results_dir = "results"
    
    print("🚀 Design Patterns Demonstration")
    print(f"📁 Output will be saved to: {results_dir}/\n")
    
    # Behavioral Patterns
    print("📊 Running Behavioral Patterns...")
    demo_observer(results_dir)
    demo_strategy(results_dir)
    
    # Creational Patterns
    print("🏭 Running Creational Patterns...")
    demo_factory(results_dir)
    demo_singleton(results_dir)
    
    # Structural Patterns
    print("🏗️  Running Structural Patterns...")
    demo_adapter(results_dir)
    demo_decorator(results_dir)
    
    # Create a summary file
    create_summary(results_dir)
    
    print(f"\n🎉 All design patterns demonstrated successfully!")
    print(f"📂 Results saved in: {results_dir}/")
    print("📄 Files created:")
    for file in os.listdir(results_dir):
        print(f"   - {file}")

def create_summary(results_dir):
    summary_file = f"{results_dir}/summary.txt"
    with open(summary_file, "w") as f:
        f.write("DESIGN PATTERNS DEMONSTRATION SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated on: {datetime.datetime.now()}\n\n")
        
        f.write("PATTERNS IMPLEMENTED:\n")
        f.write("-" * 30 + "\n")
        
        f.write("BEHAVIORAL PATTERNS:\n")
        f.write("  1. Observer Pattern - Stock Market Monitoring\n")
        f.write("  2. Strategy Pattern - Payment Processing System\n\n")
        
        f.write("CREATIONAL PATTERNS:\n")
        f.write("  3. Factory Pattern - Vehicle Manufacturing\n")
        f.write("  4. Singleton Pattern - Configuration Manager\n\n")
        
        f.write("STRUCTURAL PATTERNS:\n")
        f.write("  5. Adapter Pattern - Media Players\n")
        f.write("  6. Decorator Pattern - Coffee Shop\n\n")
        
        f.write("OUTPUT FILES:\n")
        f.write("-" * 30 + "\n")
        for file in sorted(os.listdir(results_dir)):
            if file != "summary.txt":
                f.write(f"  - {file}\n")
        
        f.write(f"\nTotal output files: {len([f for f in os.listdir(results_dir) if f != 'summary.txt'])}\n")
        f.write("All patterns executed successfully! ✅\n")

if __name__ == "__main__":
    main()