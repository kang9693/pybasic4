import socket,sys
from thread import *

try:
	listening_port = int(input("[*] Enter Listening Port Number:"))
	

except KeyboardInterrupt:
	print("\n [*] User Requested An Interrupt")
	print(" [*] Applicaton Exiting ...!!!")
	sys.exit()

max_conn = 5
buffer_size=8192