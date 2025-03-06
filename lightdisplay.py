import board
import neopixel
import time
import random

class LightDisplay:
    BLACK = (0, 0, 0)  # Define black color
    pixels = None  # Shared NeoPixel instance

    def __init__(self, brightness):
        """Initialize NeoPixels only once"""
        self.num_pixels = 10  # CPX always has 10 NeoPixels

        if LightDisplay.pixels is None:  # Only initialize once
            LightDisplay.pixels = neopixel.NeoPixel(board.NEOPIXEL, self.num_pixels, brightness=brightness, auto_write=False)

        self.pixels = LightDisplay.pixels  # Use shared instance

    def half_pattern(self, colour):
        """Lights up pixels in a symmetrical pattern"""
        positions = [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
        for pair in positions:
            for pos in pair:
                self.pixels[pos] = colour
            self.pixels.show()
            time.sleep(0.5)
        self.pixels.fill(self.BLACK)
        self.pixels.show()
    
    def light(self, side, colour):
        """Lights up specific sections based on 'side' input"""
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
        """Flashes five random pixels on and off five times"""

        if not isinstance(self.num_pixels, int):  # Ensure num_pixels is an integer
            print("Error: num_pixels is not an integer!")
            return  # Prevent function from breaking

        for _ in range(5):
            try:
                selected_pixels = random.sample(range(self.num_pixels), 5)  # ✅ Fix random.sample()
                print("Selected pixels:", selected_pixels)  # Debugging output
            except AttributeError:
                print("Error: 'random' might be overridden.")  # Debugging
                return

            for pos in selected_pixels:
                self.pixels[pos] = colour  # Light them up

            self.pixels.show()
            time.sleep(sec_interval)  # Wait

            self.pixels.fill(self.BLACK)  # Turn off
            self.pixels.show()
            time.sleep(sec_interval)  # Wait again

    def snake(self, snake_size, colour, interval):
        """Creates a moving snake pattern"""
        if not (2 <= snake_size <= self.num_pixels // 2):
            return  # Invalid snake size, terminate function
        
        for start in range(self.num_pixels - snake_size + 1):
            self.pixels.fill(self.BLACK)
            for i in range(snake_size):
                self.pixels[start + i] = colour
            self.pixels.show()
            time.sleep(interval)
