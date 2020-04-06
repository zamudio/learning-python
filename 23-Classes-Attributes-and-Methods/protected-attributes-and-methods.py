class SmartPhone():
    def __init__(self):
        self._company = 'Apple'
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        self._firmware += 1


iphone = SmartPhone()

# underscore means protected, no touchy touchy
