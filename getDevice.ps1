cd
.\devcon hwids *HDAUDIO* > deviceInfoBase.txt
Get-Content .\codecListBase.txt | Set-Content -Encoding UTF8 .\codecList.txt
Get-Content .\deviceInfoBase.txt | Set-Content -Encoding UTF8 .\deviceInfo.txt