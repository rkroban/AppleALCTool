cd
Unblock-File -Path .\DeviceManagementCmdlet.dll
Unblock-File -Path .\DeviceManagementEngine.dll
Import-module .\DeviceManagement.psd1
Get-Device | Sort-Object -Property Name | ft Name, DriverVersion, DriverProvider, IsPresent, HasProblem -AutoSize | Out-File -Append -Force "deviceInfo.txt"