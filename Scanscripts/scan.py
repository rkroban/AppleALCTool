#by @rkroban
import subprocess
subprocess.call('powershell.exe -ExecutionPolicy Unrestricted -file "getDevice.ps1"', shell=True)
count = 0
realtk = 0
with open("deviceInfo.txt") as devices:
    for line in devices:
        if line != "\n":
            count += 1
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if 'Realtek' in line:
            i += 3
            realtk = i
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if i == realtk:
            if 'DEV_' in line:
                codec = {line[line.index("DEV_") + 4:line.index("DEV_") + 8]}
hdcodec = ''.join(codec)
with open("codecList.txt") as codecs:
    for line in codecs:
        if hdcodec in line:
            print('your codec id, codec, patch, possible layout ids, minimum kernel, and maximum kernel are')
            print(f'{line}')
            break