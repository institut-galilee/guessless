#!/usr/bin/env python
from samplebase import SampleBase


class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):
        max_brightness = self.matrix.brightness
        count = 0

        while (50):
            if self.matrix.brightness < 1:
                self.matrix.brightness = max_brightness
                count += 1
            else:
                self.matrix.brightness -= 1

            if count % 4 == 0:
                self.matrix.Fill(255, 255, 255)
            elif count % 4 == 1:
                self.matrix.Fill(255, 255, 255)
            elif count % 4 == 2:
                self.matrix.Fill(255, 255, 255)
            elif count % 4 == 3:
                self.matrix.Fill(255, 255, 255)

            self.usleep(20 * 1000)

# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()
