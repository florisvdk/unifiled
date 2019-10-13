import time
from unifiled import unifiled

# ask for needed info

print("This is the unifiled python module example/test script.")
print("Led Controller ip:")
ip = str(input())
print("Led Controller port (20443):")
port = str(input())
print("Led Controller user:")
user = str(input())
print("Led Controller password:")
password = str(input())

# login first

api = unifiled(ip, port, username=user, password=password, debug=True)

print("login succesfull")

# get device list

devices = api.getdevices()

print("Got " + str(len(devices)) + " device(s) succesfully\n\n")

# loop trugh devices

print('  Devices:')

i = 0

for device in devices:
    print(str(i) + '   Model: ' + device['info']['model'] + 'Name: ' + device['name'] + ' Type: ' + device['type'])
    print('      Status[ Brightness: ' + str(device['status']['led']) + ' State: ' + str(device['status']['output']) + ' Online: ' + str(device['isOnline']) + ' ]')
    i += 1

# ask for input

print("enter the number before the device to edit:")
devicetoset = int(input())
print("enter the brightness(0-100):")
brightness = int(input())
print("Should the output be on(1) or off(0):")
output = int(input())

deviceid = devices[devicetoset]['id']

# set brightness on device

if api.setdevicebrightness(deviceid, brightness) == True:

    print("Set brightness succesfully")

else:

    print("Could not set brightness")

# set output on device

if api.setdeviceoutput(deviceid, output) == True:

    print("Set output succesfully")

else:

    print("Could not set output")

# get groups

groups = api.getgroups()

if groups == False:

    print("Could not get groups, check settings or server")
    exit()

print("Got groups succesfully")

# loop trugh groups

i = 0

while i < len(groups):

    print(str(i) + "   Group name: " + groups[i]['name'])
    print("      Status[ Brightness: " + str(groups[i]['led']) + " State: " + str(groups[i]['output']) + " Devices turned on: " + str(groups[i]['devicesTurnedOn']) + " ]")

    print("      Devices:")

    # loop trugh devices in group

    j = 0

    while j < len(groups[i]['devices']):

        print('        ' + groups[i]['devices'][j]['name'])

        #devices in group

        j += 1

    i += 1

print("This is the end of the demo.")
