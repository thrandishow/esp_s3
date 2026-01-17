from machine import Pin, SPI
import time
import ili9341
import xglcd

font = xglcd.XglcdFont("Unispace12x24.c", 12, 24)
bl = Pin(45, Pin.OUT)
bl.on()

spi = SPI(1, sck=Pin(12), mosi=Pin(11), miso=Pin(13))
display = ili9341.Display(
    spi,
    cs=Pin(10),
    dc=Pin(46),
    rst=Pin(0),
    width=240,
    height=320,
    rotation=0,
)
display.write_cmd(0x21)
display.clear()
