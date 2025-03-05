import adafruit_lis3dh
import busio
import board
from lightdisplay import LightDisplay

class SensorLightDisplay(LightDisplay):
    def __init__(self, brightness):
        """Initialize sensor and NeoPixels without re-initializing NeoPixels"""
        super().__init__(brightness)  # Use existing NeoPixel setup

        try:
            # Setup accelerometer
            i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)

            # Try initializing the accelerometer at 0x18 first, if that fails, try 0x19
            try:
                self.accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x18)
                print("Accelerometer initialized at 0x18")
            except ValueError:
                self.accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
                print("Accelerometer initialized at 0x19")

            # Set accelerometer range for sensitivity
            self.accelerometer.range = adafruit_lis3dh.RANGE_2_G  

        except RuntimeError as e:
            print("Error initializing accelerometer:", e)
            self.accelerometer = None  # Prevent crashes

    def light(self, colour):
        """Control NeoPixels based on accelerometer tilt"""
        
        if self.accelerometer is None:
            print("Accelerometer not initialized!")  # Debugging
            return  # Exit function if there's no accelerometer

        # Get real-time acceleration values
        x, y, _ = self.accelerometer.acceleration
        print(f"Acceleration X: {x}, Y: {y}")  # Debugging output
        
        if x < -3 and x < y:
            positions = [6, 7, 8]  # Left tilt
        elif x > 3 and x > y:
            positions = [1, 2, 3]  # Right tilt
        elif y > 3 and y > x:
            positions = [4, 5]  # Forward tilt
        elif y < -3 and y < x:
            positions = [0, 9]  # Backward tilt
        else:
            self.pixels.fill(self.BLACK)
            self.pixels.show()
            return

        for pos in positions:
            self.pixels[pos] = colour
        self.pixels.show()




    
    def control_feedback_y(self, acceleration_y):
        """Maps Y-axis acceleration to color intensity"""
        if -9.81 <= acceleration_y <= 9.81:
            intensity = int((acceleration_y + 9.81) / 19.62 * 255)
            self.pixels.fill((intensity, 0, 255 - intensity))
            self.pixels.show()
