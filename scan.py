#by @rkroban
import subprocess
subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -file "getDevice.ps1"', shell=True)
count = 0
realtk = 0
with open("deviceInfo.txt") as devices:
    for line in devices:
        if line != "\n":
            count += 1
print('Total Lines', count)
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if 'Realtek' in line:
            i += 3
            realtk = i
            print(f'{i}')
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if i == realtk:
            print(f'{line}')
            if 'DEV_' in line:
                print(f'{line.index("DEV_")}')
                print(f'{line[line.index("DEV_") + 4:line.index("DEV_") + 8]}')
                codec = {line[line.index("DEV_") + 4:line.index("DEV_") + 8]}