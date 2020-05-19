# Remote-Terminal

This project enables one computer on a network to run commands on the terminal of another computer connected through the network.
The connection is established through socket programming. The connection can be either internet or intranet.

This repository contains two python files:
1. commander.py
2. terminal.py

terminal.py:
This file is executed in the system on whose terminal the commands are executed.
This files opens a socket for connection and waits for the commander to send commands.
Once connected to the commander, it starts executing the commands received from the commander system.
Commanding starts when commander sends "ls" and stops when the commander send "shutup".

commander.py:
This file is executed in the system that send the commands to terminal of another system.
This get connected to the socket opened by the terminal system using its IP address and port number and starts sending commands.
The commanding stops when the user enters "shutup".
