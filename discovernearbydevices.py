import bluetooth
import playsound
while True:
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))
    if len(nearby_devices) == 0:
        playsound.playsound('C:/Users/yehia/Desktop/waiting.wmv')
    elif len(nearby_devices) > 0:
        playsound.playsound('C:/Users/yehia/Desktop/found.wmv')
        for addr, name in nearby_devices:
            print("  {} - {}".format(addr, name))
