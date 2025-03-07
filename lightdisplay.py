import board
import neopixel
import time
from random import randint  

class LightDisplay:
    BLACK = (0, 0, 0)  
    pixels = None  

    def __init__(self, brightness):
        self.num_pixels = 10  

        if LightDisplay.pixels is None:  
            LightDisplay.pixels = neopixel.NeoPixel(board.NEOPIXEL, self.num_pixels, brightness=brightness, auto_write=False)

        self.pixels = LightDisplay.pixels  

    def half_pattern(self, colour):
        positions = [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
        for pair in positions:
            for pos in pair:
                self.pixels[pos] = colour
            self.pixels.show()
            time.sleep(0.5)
        self.pixels.fill(self.BLACK)
        self.pixels.show()

    def light(self, side, colour):
        mapping = {
            0: [1, 2, 3],
            1: [6, 7, 8],
            2: [4, 5],
            3: [0, 9]
        }
        if side in mapping:
            for pos in mapping[side]:
                self.pixels[pos] = colour
            self.pixels.show()

    def random_light(self, colour, sec_interval):

        for _ in range(5):
            indices = []
            
            while len(indices) < 5:
                num = randint(0, self.num_pixels - 1)  
                if num not in indices:
                    indices.append(num)
            
            for i in indices:
                self.pixels[i] = colour  

            self.pixels.show()
            time.sleep(sec_interval)

            for i in indices:
                self.pixels[i] = self.BLACK  

            self.pixels.show()
            time.sleep(sec_interval)

    def snake(self, snake_size, colour, interval):
        if not (2 <= snake_size <= self.num_pixels // 2):
            return  

        for start in range(self.num_pixels - snake_size + 1):
            self.pixels.fill(self.BLACK)
            for i in range(snake_size):
                self.pixels[start + i] = colour
            self.pixels.show()
            time.sleep(interval)
