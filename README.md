# AppleALCTool
Work in progress, will eventually be cabale of building AppleALC.kext while also providing info on audio codec and layout-id's

NOTE: Will only work with Realtek Audio Codecs upon completion. Additional support may be added later

**Requirements:**
* a realtek soundcard 


* a intel processor, AMD has no support for it's microphones, but has functional audio (This doesn't matter right now since the script can't build kernel extensions yet)


* Python 3.11 or higher installed (you can get python [here](https://www.python.org/downloads/))


* windows 10 or higher


**What's new:**


* Scan.py now outputs the audio codec and layoud ids of the user's device



**Credits:**


* [Acidanthera](https://github.com/acidanthera/AppleALC) for AppleALC

* [Python](https://www.python.org/) for Python

* [Microsoft](https://www.microsoft.com/) for Unblock-File cmdlet

* [Microsoft](https://www.microsoft.com/) for DevCon.exe