import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """
    Provides a Smiley with an angry expression
    """
    def __init__(self):
        super().__init__(complextion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Renders an angry downturned mouth
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes with subtle angry eyebrows
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.get_complextion()

        # Subtle inward eyebrows
        eyebrows = [9, 14]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def blink(self, delay=0.25):
        """
        Blinks the smiley's eyes once
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()