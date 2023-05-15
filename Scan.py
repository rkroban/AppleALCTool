import List
import subprocess
power = subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -file "getDevice.ps1"', shell=True)