Python on microcontrollers
==========================

There has been various attempts to port Python on microcontrollers. The power
of interpreted language cannot be kept in darkness.

Projects like Pymite, WiPy, micropython have demonstrated the concept on real
microcontrollers. Among the mentioned projects ``micropython`` offers port for
most affordable hardware, ``esp8266``.

The esp8266 family can be programmed in ``lua``, ``AT``, ``C`` as well. In fact
Python implementation is under rapid development.

Specifications of esp8266 (version 12)
--------------------------------------

#. High performance wireless 32 bit wireless SoC

#. 2.4GHz 802.11 b/g/n, Wi-Fi Direct(P2P), soft-AP, RTC

#. SDIO 2.0(Secure DIgital IO), SPI, UART

#. 16 GPIO

#. ~50kB of RAM (not mentioned clearly in datasheet)

#. ~1MB of Flash memory (ROM)

Application of esp8266
----------------------

#. Smart power plugs

#. IP Cameras

#. Sensor networks

#. Wearable electronics

#. Home automation

Installation
------------

The development environment available for GNU/Linux only. One needs following
repositories setup (read the instructions provided in respecive project &
install all packages) ::

	https://github.com/pfalcon/esp-open-sdk

	https://github.com/micropython/micropython.git

Hardware Setup
--------------

#. esp8266 development board

#. USB-to-serial cable

And make sure GPIO-0 & GPIO-15 are set according to given table.

 +---------+--------+--------+-------+-------------------------------+
 | GPIO 15 | GPIO 0 | GPIO 2 | Mode  | Description                   |
 +=========+========+========+=======+===============================+
 | 0       | 0      | 1      | UART  | Download code from UART       |
 +---------+--------+--------+-------+-------------------------------+
 | 0       | 1      | 1      | Flash | Boot from SPI Flash           |
 +---------+--------+--------+-------+-------------------------------+
 | 1       | x      | x      | SDIO  | Boot from sdcard (not tested) |
 +---------+--------+--------+-------+-------------------------------+


Loading micropython to esp8266's ROM
------------------------------------

Connect esp8266's Rx line with Tx of USB-to-serial cable and vice-versa.
Edit your `micropython/esp8266/Makefile` and add your USB-to-serial path, in my
case it was ``/dev/ttyUSB0``.

To install micropython you need to be in ``UART`` mode. Execute ::

	make deploy

to compile micropython and install/upload it to esp8266's ROM. This process
might take upto 2 minutes.

Once done, you need to switch to ``Flash`` mode (see table above). Open minicom
with baud rate ``115200 8N1 bps`` and ``No hardware/software flow control``.

Hit enter to find Python prompt ``>>>``. That's all, have fun !!!

Running a Python script
-----------------------

To run a Python script simply write the program in
`micropython/esp8266/scripts/main.py`, this will get compiled at the build time.




