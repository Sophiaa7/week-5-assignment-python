# Define the parent class: SamsungPhone
class SamsungPhone:
    def __init__(self, model, year, battery_capacity, storage):
        """
        Initialize a SamsungPhone object.

        Args:
            model (str): Phone model.
            year (int): Release year.
            battery_capacity (int): Battery capacity in mAh.
            storage (int): Storage capacity in GB.
        """
        self.model = model
        self.year = year
        self.battery_capacity = battery_capacity
        self.storage = storage
        self.is_charged = False

    def charge(self):
        """Charge the phone."""
        self.is_charged = True
        print(f"{self.model} is now charged.")

    def make_call(self, number):
        """Make a call."""
        if self.is_charged:
            print(f"Calling {number} from {self.model}...")
        else:
            print(f"{self.model} is not charged. Please charge before making a call.")

    def send_text(self, number, message):
        """Send a text message."""
        if self.is_charged:
            print(f"Sending '{message}' to {number} from {self.model}...")
        else:
            print(f"{self.model} is not charged. Please charge before sending a text.")


# Define the child class: SamsungGalaxy (inherits from SamsungPhone)
class SamsungGalaxy(SamsungPhone):
    def __init__(self, model, year, battery_capacity, storage, camera_resolution):
        """
        Initialize a SamsungGalaxy object.

        Args:
            model (str): Phone model.
            year (int): Release year.
            battery_capacity (int): Battery capacity in mAh.
            storage (int): Storage capacity in GB.
            camera_resolution (str): Rear camera resolution.
        """
        super().__init__(model, year, battery_capacity, storage)
        self.camera_resolution = camera_resolution

    def take_picture(self):
        """Take a picture."""
        if self.is_charged:
            print(f"Taking a picture with {self.model}'s {self.camera_resolution} camera...")
        else:
            print(f"{self.model} is not charged. Please charge before taking a picture.")


# Example usage:
if __name__ == "__main__":
    # Create SamsungPhone objects
    samsung_s10 = SamsungPhone("Galaxy S10", 2019, 4100, 128)
    samsung_s20 = SamsungPhone("Galaxy S20", 2020, 4500, 256)

    # Create SamsungGalaxy objects
    samsung_galaxy_s21 = SamsungGalaxy("Galaxy S21", 2021, 5000, 512, "50MP")
    samsung_galaxy_s22 = SamsungGalaxy("Galaxy S22", 2022, 5500, 1024, "108MP")

    # Test methods
    samsung_s10.charge()
    samsung_s10.make_call("08123456789")
    samsung_s10.send_text("08123456789", "Hello from Samsung S10!")

    samsung_galaxy_s21.take_picture()
    samsung_galaxy_s21.send_text("08123456789", "Hello from Samsung Galaxy S21!")