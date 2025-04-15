#Author: Moleboheng Madela
#Date: 2025-04-15

# Activity 1: Design Your Own Class

# Step 1: Define a general class called Device
# This is the parent class or "base" class

class Device:
    # Constructor to initialize the brand and model
    def __init__(self, brand, model):
        self.brand = brand     # Instance variable to hold brand name
        self.model = model     # Instance variable to hold model name

    # Method to simulate turning the device ON
    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    # Method to simulate turning the device OFF
    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF.")

        # Step 2: Define a specific class called Smartphone that INHERITS from Device

class Smartphone(Device):
    # Constructor that adds more attributes: OS and Storage
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor for brand and model
        self.os = os                    # Operating System (Android, iOS, etc.)
        self.storage = storage          # Storage capacity in GB

    # Method to simulate taking a photo
    def take_photo(self):
        print(f"{self.brand} {self.model} is taking a photo.")

    # Method to simulate making a phone call
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}.")

    # Method to display smartphone information
    def show_info(self):
        print(f"\nSmartphone Info:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Operating System: {self.os}")
        print(f"Storage: {self.storage} GB\n")

# Step 3: Create an object (instance) of Smartphone and interact with it

# Creating a new smartphone with custom values
my_phone = Smartphone("Samsung", "Galaxy S22", "Android", 256)

# Using the object to call its methods
my_phone.show_info()         # Shows all the phone info
my_phone.power_on()          # Turn the phone on (inherited from Device)
my_phone.take_photo()        # Take a photo
my_phone.make_call("0123456789")  # Make a call
my_phone.power_off()         # Turn the phone off