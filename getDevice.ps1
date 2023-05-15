cd
Import-Module .\PSCmdlet.psd1 –Verbose
Get-Device | Sort-Object -Property Name | ft Name, DriverVersion, DriverProvider, IsPresent, HasProblem -AutoSize | Out-File -Append -Force "FileListName.txt"