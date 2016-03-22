# ChromePassDumper
Specific and simple tool for educational purposes: demonstrating live dumping of Chrome passwords or practising a simulated scenario of "two-step offline attack" for password database stealing.

This tool is basically a script that dumps passwords stored in Google Chrome default profile of the live user. Since chrome is at this time ciphering the password fields of the logindata SQLITE file, the script retrieves the ciphered BLOB from database and then requests the decription of such blob to the Local Security Authority through Windows' Data Protection API.

Since DPAPI uses several ciphering layers, and the first of them is derived (400 rounds PBKDF2) from user password, access to DPAPI decryption functions is not possible if the user is not logged in the live system, making the decryption of Chrome passwords a matter of slow, unfeasible bruteforcing.

A sample auxiliary BAT script is provided for demonstration purposes as a launcher/dropper tool, which can circunvent the forementioned limitation using a "two-step offline attack" when target computer has not full disk encryption, which would be like this:

*STEP ONE*
1) "Compile" this script to EXE using PyInstaller tool inside a Python 3.x valid installation (http://www.pyinstaller.org/).
2) Access the target filesystem with a live linux system or any similar tool that enables you to read/write target filesystem.
3) Copy the launcher BAT to profiles start menu "start" folder (*%APPDATA%/Microsoft/Windows/Start menu/Start*), so it executes on next windows boot.
4) Copy the compiled EXE to %APPDATA% folder directly.
5) Unmount the filesystem cleanly and await for the user to log in at least one time. 

When user logs in, BAT file will launch, calling the EXE'd script, which will make the password dumping process. BAT file will erase itself so EXE file will never be executed a second time and startup environment will be clean again.

*STEP TWO*
1) Access the target filesystem with a live linux system or any similar tool that enables you to read/write target filesystem.
2) Retrieve the password dump file: *%APPDATA%/audit.log*.
3) Clean evidence (dump file and EXE file).

#DISCLAIMER
These materials are for educational and research purposes only. Do not attempt to violate the law with anything contained here. If this is your intention, neither the author or the organization presenting this material is going to accept responsibility for your actions.
