import time, unifiled

# ask for needed info

print("This is the unifiled python module example/test.")
print("Led Controller ip:")
ip = input()
print("Led Controller port (20443):")
port = input()
print("Led Controller user:")
user = input()
print("Led Controller passord:")
password = input()

# login first

session = unifiled.Login.ledlogin(user, password, ip, port)

if session == False:

    print("Coudl not login, check settings or server")
    exit()

print("login succesfull")

# get device list

devices = unifiled.Get.leddevices(session, ip, port)

if devices == False:

    print("Coudl not get devices, check settings or server")
    exit()

print("Got " + str(len(devices)) + " device(s) succesfully\n\n")

# loop trugh devices

print('  Devices:')

i = 0

while i < len(devices):
    print(str(i) + '   Model: ' + devices[i]['info']['model'] + 'Name: ' + devices[i]['name'] + ' Type: ' + devices[i]['type'])
    print('      Status[ Brightness: ' + str(devices[i]['status']['led']) + ' State: ' + str(devices[i]['status']['output']) + ' Online: ' + str(devices[i]['isOnline']) + ' ]')
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

if unifiled.Set.leddevicesetbrightness(deviceid, brightness,session, ip, port) == True:

    print("Set brightness succesfully")

else:

    print("Could not set brightness")

# set output on device

if unifiled.Set.leddevicesetoutput (deviceid, output, session, ip, port) == True:

    print("Set output succesfully")

else:

    print("Could not set output")

# get groups

groups = unifiled.Get.ledgroups(session, ip, port)

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
