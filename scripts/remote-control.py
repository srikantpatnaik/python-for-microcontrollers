# This script will run on boot
# testing with esp8266 by Srikant
# Thanks to github user 'atalax' and many others

# License: GNU GPLv3

import esp
import sys
import network
import gc
from pyb import Pin

ssid = 'your-wifi-ssid'
passwd = 'ofcourse-password'

pin12_B = Pin(12, Pin.OUT_PP)
pin12_B.low()

pin13_G = Pin(13, Pin.OUT_PP)
pin13_G.low()

# Pin 15 is RED LED on board
pin15_R = Pin(15, Pin.OUT_PP)

def onnewclient(s):
    s.onrecv(onclientdata)
    s.onsent(onclientsent)

def onclientdata(s, d):
    dp = d.split()
    b = dp[-1]
    if b.endswith('ON'):
        pin15_R.high()
    elif b.endswith('OFF'):
	pin15_R.low()
    path = dp[1].format("ascii")
    if path == "/":
	s.send("HTTP/1.0 200 OK\r\n"
               "Server: Micropython for ESP8266\r\n"
               "Content-Type: text/html\r\n"
               "Connection: close\t\n"
               "\r\n"
		"<html>\r\n"
               "<head><h1 align='center'>Python for esp8266 - SciPy India 2015</h1></head>\r\n"
		"<body bgcolor='#ccff99'>\r\n"
	       "<form align='center' action='' method='post'>\r\n"
		"<fieldset>\r\n"
		"<legend style='color:red'>Red LED Control</legend>\r\n"
		"<input type='radio' name='LED' value='ON'> ON\r\n"
		"<input type='radio' name='LED' value='OFF'> OFF<br>\r\n"
		"</fieldset>\r\n"

		"<input type='submit' value='Submit'>\r\n"
		"</form>\r\n"
		"</body>\r\n"
	       	)
    else:
        s.send("HTTP/1.0 404 OK\r\n"
               "Server: Micropython for ESP8266\r\n"
               "Content-Type: text/html\r\n"
               "Connection: close\r\n"
               "\r\n"
               "<h1>:(</h1>")

def onclientsent(s):
    s.close()

network.connect(ssid, passwd)
socket = esp.socket()
socket.onconnect(onnewclient)
gc.collect()
socket.bind(("", 80))
socket.listen(5)
