import os

class ConfigurationManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self._config = {
            "database_url": "localhost:5432/mydb",
            "api_key": "default_api_key_123",
            "max_connections": 100,
            "debug_mode": False,
            "timeout": 30
        }
    
    def get(self, key: str):
        return self._config.get(key)
    
    def set(self, key: str, value):
        self._config[key] = value
    
    def get_all_config(self):
        return self._config.copy()
    
    def __str__(self):
        config_str = "\n".join([f"{k}: {v}" for k, v in self._config.items()])
        return f"Configuration:\n{config_str}"

def demo_singleton(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/singleton_config.txt", "w") as f:
        f.write("=== Singleton Pattern: Configuration Manager ===\n\n")
        
        # First instance
        config1 = ConfigurationManager()
        f.write("Config 1 - Database URL: " + str(config1.get("database_url")) + "\n")
        
        # Modify via first instance
        config1.set("api_key", "new_secret_key_456")
        config1.set("debug_mode", True)
        config1.set("timeout", 60)
        
        # Second instance - should have same modified data
        config2 = ConfigurationManager()
        f.write("Config 2 - API Key: " + str(config2.get("api_key")) + "\n")
        f.write("Config 2 - Debug Mode: " + str(config2.get("debug_mode")) + "\n")
        f.write("Config 2 - Timeout: " + str(config2.get("timeout")) + "\n\n")
        
        # Verify they are the same instance
        f.write(f"Same instance? {config1 is config2}\n\n")
        
        # Show all configuration
        f.write("All Configuration:\n")
        f.write(str(config2) + "\n\n")
        
        f.write("Singleton pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_singleton()