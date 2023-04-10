#!/usr/bin/env python3

import subprocess

svc = "sshd"

check_cmd = ["ps", "-C", svc]
# service_check is a variable that gets the exit code from ps -C sshd
service_check = subprocess.call(check_cmd)

if service_check == 0:
    print("Service is running")
else:
    print("The Service is NOT running.")
    print("Starting it ...")
    try:
        # note: check_output fails with an exception if the service 
        # is not found
        # where as .call will not throw an exception even though
        # it failed
        subprocess.check_output(["systemctl", "start", "ssh"])
    except subprocess.CalledProcessError as e:
        print("There was an error starting the process")
        print(e)
        exit(1)

    subprocess.call(check_cmd)

    # to install this service
    # sudo apt-get install openssh-server
    # to remove it
    # sudo apt remove openssh-server