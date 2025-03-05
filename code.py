# code.py
import time
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay

# Test NeoPixel patterns
light_display = LightDisplay(0.5)
sensor_display = SensorLightDisplay(0.5)

# Test methods (commented out to avoid memory issues)
#light_display.half_pattern((255, 0, 0))  # Red half pattern
#light_display.light(1, (0, 255, 0))  # Green side pattern
#light_display.random_light((0, 0, 255), 0.3)  # Blue random pattern
#light_display.snake(3, (255, 255, 0), 0.2)  # Yellow snake pattern

# Simulate accelerometer-based lighting
#sensor_display.light([-4, 2], (255, 0, 0))  # Tilted left - Red
# sensor_display.control_feedback_y(-5)  # Adjust color based on tilt

