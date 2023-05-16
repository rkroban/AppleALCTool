cd
.\devcon hwids *HDAUDIO* > deviceInfoBase.txt
Get-Content .\deviceInfoBase.txt | Set-Content -Encoding UTF8 .\deviceInfo.txt