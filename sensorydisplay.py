# sensorlightdisplay.py
import adafruit_lis3dh
import adafruit_lis3dh
import busio
import board
from lightdisplay import LightDisplay

class SensorLightDisplay(LightDisplay):
    def __init__(self, brightness):
        """Initialize sensor without re-initializing NeoPixels"""
        super().__init__(brightness)  # Use existing NeoPixel setup

        # Setup accelerometer (currently disabled to test snake)
        self.accelerometer = None  # Temporarily disabled for debugging

    
    def light(self, acceleration, colour):
        """Control NeoPixels based on accelerometer tilt"""
        x, y, _ = acceleration
        if x < -3 and x < y:
            positions = [6, 7, 8]
        elif x > 3 and x > y:
            positions = [1, 2, 3]
        elif y > 3 and y > x:
            positions = [4, 5]
        elif y < -3 and y < x:
            positions = [0, 9]
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
