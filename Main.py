#by @rkroban
import List
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
    for line in devices:
        realtk_index = line.find('Realtek')
        if realtk_index < 0:
            realtktmp += 1
        else:
            realtktmp += 1
            realtk = realtktmp
            print(f'Realtek hardware ids starting at index {realtk_index} of line {realtk}')
#search the lines after 'realtk' to fint he audio codec
print('now checking the data to find the audio codec')