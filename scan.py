#by @rkroban
import subprocess
#execute the powershell script with no restrictions until the script is complete
subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -file "getDevice.ps1"', shell=True)
#find the number of lines with text in the output file
count = 0
realtk = 0
with open("deviceInfo.txt") as devices:
    for line in devices:
        if line != "\n":
            count += 1
print('Total Lines', count)
#find the line where the Realtek Hardware ids start in the output file and record it as 'realtk'
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if 'Realtek' in line:
            i += 3
            realtk = i
            print(f'{i}')
#print the line containing the codec id
with open("deviceInfo.txt") as devices:
    for i, line in enumerate(devices):
        if i == realtk:
            print(f'{line}')
            #find the index of DEV_ at line and print the codec id
            if 'DEV_' in line:
                print(f'{line.index("DEV_")}')
                print(f'{line[line.index("DEV_") + 4:line.index("DEV_") + 8]}')
                codec = {line[line.index("DEV_") + 4:line.index("DEV_") + 8]}