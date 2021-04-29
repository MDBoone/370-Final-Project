import time
from rpi_ws281x import *
LED_COUNT = 8
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

class Led2:
    def __init__(self):
        self.ORDER = "RGB"
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
    def LED_TYPR(self, order, R_G_B):
        B=R_G_B & 255
        G=R_G_B >> 8 & 255
        R=R_G_B >> 16 & 255
        Led_type=["GRB", "GBR", "RGB", "RBG", "BRG", "BGR"]
        color = [Color(G,R,B),Color(G,B,R),Color(R,G,B),Color(R,B,G),Color(B,R,G),Color(B,G,R)]
        if order in Led_type:
            return color[Led_type.index(order)]
    def ledIndex(self,index,R,G,B):
        color=self.LED_TYPR(self.ORDER,Color(R,G,B))
        for i in range(8):
            if index & 0x01 == 1:
                self.strip.setPixelColor(i,color)
                self.strip.show()
            index=index >> 1

