import List
import subprocess
subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -file "getDevice.ps1"', shell=True)
with open("deviceInfo.txt") as devices:
    count = 0
    for line in devices:
        if line != "\n":
            count += 1
print('Total Lines', count)
with open("deviceInfo.txt") as devices:
    realtk = 0
    for line in devices:
        if line == "Realtek":
            print('Realtek Hardware IDs found at line', realtk)
        else:
            realtk += 1
