cd
Unblock-File -Path .\DeviceManagement\DeviceManagementCmdlet.dll
Unblock-File -Path .\DeviceManagement\DeviceManagementEngine.dll
Import-module .\DeviceManagement\DeviceManagement.psd1
Get-Device | Sort-Object -Property Name | ft Name, DriverVersion, DriverProvider, -AutoSize | Out-File -Append -Force "deviceInfo.txt" -Encoding UTF8