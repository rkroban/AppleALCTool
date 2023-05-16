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
    realtktmp = 0
    printline = []
    for line in devices:
        realtk_index = line.find('DEV_0')
        if realtk_index < 0:
            realtktmp += 1
        else:
            realtktmp += 3
            realtk = realtktmp
            print(f'Realtek codec ids starting at line {realtk}')