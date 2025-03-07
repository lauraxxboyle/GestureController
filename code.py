import time
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay


light_display = LightDisplay(0.5)
sensor_display = SensorLightDisplay(0.5)  


while True:
    #light_display.half_pattern((255, 0, 0))  
    #light_display.light(1, (0, 255, 0)) 
    #light_display.random_light((0, 0, 255), 0.3)  
    #light_display.snake(3, (255, 255, 0), 0.2)  

    #sensor_display.light((255, 255, 0))  
    
   
    #acceleration_y = sensor_display.accelerometer.acceleration[1]
    #sensor_display.control_feedback_y(acceleration_y)  
    
    #time.sleep(0.1)  
