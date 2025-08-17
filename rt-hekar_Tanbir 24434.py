import socket
import pyfiglet
from termcolor  import colored

benar =   colored(pyfiglet.figlet_format("rt hekar"),"green")
print(benar)

domein = input (" inter your URL : ")
ip = socket.gethostbyname(domein)
print (ip)







