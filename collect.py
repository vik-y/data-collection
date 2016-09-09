import os
import re

def ping(url):
    temp = os.popen("ping -c 10 -i 0.2 -W 2 %s" % (url)).read()
    return temp


def wifiInterfaceName():
    temp = os.popen("iwconfig").read() # Runs and gets iwconfig command output
    result = re.search(".*802", temp)

    if result:
        interfaceName = result.group().split()[0]
        return interfaceName
    else:
        print "No wifi interface found"
        return 0

def format(text):
    return "\n"+text+"\n"
# Get the wifi interface name.
# Cant assume it to be wlan0
wifi = wifiInterfaceName()

# If wifi is not connected then terminate the program
if wifi==0:
    print """
    This script works only when you are connected to wifi.
    Please turn on your wifi and then try to run this script.
    If you are unable to connect to wifi at all then mention it
    in the email.
    """
    exit()

urls = ['google.com', 'facebook.com', 'iiitb.ac.in']

output = open("outputData.txt", "w")

for url in urls:
    print "Collecting ping stats for %s" % (url)
    result = ping(url)
    output.write(format(result))

# Data of all other commands here
print "Collecting ifconfig"
ifconfig = os.popen("ifconfig").read()
print "Collecting iwconfig"
iwconfig = os.popen("iwconfig").read()
print "Collecting routes"
routes = os.popen("route -n").read()

output.write("\n\nIFCONFIG OUTPUT\n")
output.write(ifconfig)

output.write("\n\nIWCONFIG OUTPUT\n")
output.write(iwconfig)

output.write("\n\nROUTES\n")
output.write(routes)

output.close()
