import List
import DeviceManager
dm = DeviceManager()
dm.root.rescan()
devices = dm.all_devices
for device in devices:
    print(device)