import time
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay

# Test NeoPixel patterns
light_display = LightDisplay(0.5)
sensor_display = SensorLightDisplay(0.5)  # ✅ Only one instance

# Test methods (commented out to avoid memory issues)
#light_display.half_pattern((255, 0, 0))  # Red half pattern
#light_display.light(1, (0, 255, 0))  # Green side pattern
#light_display.random_light((0, 0, 255), 0.3)  # Blue random pattern
#light_display.snake(3, (255, 255, 0), 0.2)  # Yellow snake pattern

#print("Starting accelerometer-based lighting...")

# Continuous loop to update lights based on tilting
#while True:
    #sensor_display.light((255, 255, 0))  # Adjust LEDs based on tilt (Red)
    
    # Adjust brightness based on tilt feedback
    #acceleration_y = sensor_display.accelerometer.acceleration[1]
    #sensor_display.control_feedback_y(acceleration_y)  
    
    #time.sleep(0.1)  # ✅ Prevents CPU overload
