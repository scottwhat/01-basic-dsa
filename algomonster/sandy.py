from datetime import date

class Employee:
    # Class variable shared by all instances
    company = "TechCorp"
    raise_rate = 1.04

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    # Regular instance method - needs an instance
    def apply_raise(self):
        self.salary = self.salary * self.raise_rate
    
    # Class method - works with the class itself
    @classmethod
    def from_string(cls, employee_str: str):
        """Alternative constructor using class method"""
        name, salary = employee_str.split('-')
        return cls(name, float(salary))
    
    @classmethod
    def change_raise_rate(cls, new_rate: float):
        """Modify class-level attribute"""
        cls.raise_rate = new_rate
    
    # Another common use case - factory method
    @classmethod
    def create_developer(cls, name: str, salary: float, language: str):
        """Factory method to create a Developer"""
        dev = Developer(name, salary)
        dev.language = language
        return dev
    
    def __str__(self):
        return f"{self.name} (${self.salary:,.2f})"

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)
        self.language = None

# Example Usage:

# 1. Regular instance creation
emp1 = Employee("John", 50000)
print(emp1)  # John ($50,000.00)

# 2. Using class method as alternative constructor
emp_data = "Alice-60000"
emp2 = Employee.from_string(emp_data)
print(emp2)  # Alice ($60,000.00)

# 3. Modifying class-level attribute
print(f"Current raise rate: {Employee.raise_rate}")  # 1.04
Employee.change_raise_rate(1.05)
print(f"New raise rate: {Employee.raise_rate}")      # 1.05

# 4. Factory method for creating specific types
dev1 = Employee.create_developer("Bob", 70000, "Python")
print(f"{dev1.name} codes in {dev1.language}")  # Bob codes in Python

# Real-world example with dates
class Date:
    def __init__(self, year: int, month: int, day: int):
        self.date = date(year, month, day)
    
    @classmethod
    def from_iso(cls, iso_date: str):
        """Create from ISO format (YYYY-MM-DD)"""
        year, month, day = map(int, iso_date.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Get today's date"""
        today = date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return self.date.strftime("%B %d, %Y")

# Using the Date class
date1 = Date(2025, 8, 9)                    # Regular constructor
date2 = Date.from_iso("2025-08-09")         # Class method constructor
date3 = Date.today()                        # Class method factory

print(date1)  # August 09, 2025
print(date2)  # August 09, 2025
print(date3)  # Current date

# Common use case - Configuration
class Config:
    _instance = None
    
    def __init__(self):
        self.api_key = None
        self.debug_mode = False
    
    @classmethod
    def get_instance(cls):
        """Singleton pattern using class method"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def from_dict(cls, config_dict: dict):
        """Create configuration from dictionary"""
        instance = cls()
        instance.api_key = config_dict.get('api_key')
        instance.debug_mode = config_dict.get('debug_mode', False)
        return instance

# Using the Config class
config1 = Config.get_instance()  # Get singleton instance
config2 = Config.get_instance()  # Same instance as config1
print(config1 is config2)  # True

# Create from dictionary
config_data = {
    'api_key': 'abc123',
    'debug_mode': True
}
config3 = Config.from_dict(config_data)

class Superhero:
    training_level = 1  # Class attribute
    
    def __init__(self, name: str, power: str):
        self.name = name         # Instance attribute
        self.power = power       # Instance attribute
        
    @classmethod
    def upgrade_training(cls) -> None:
        cls.training_level += 1
        print(f"All heroes now at training level {cls.training_level}")