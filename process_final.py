#!/usr/bin/python

# Compile bytecode:
# pycompile process2.py

import os
import string
import subprocess
import sys
import psutil
import datetime

v_service="winbindd"
v_process="winbindd"
v_consume=90.0
v_psutilversion = 3
f_log = open('logfile.log','a')
p_version = sys.version_info[0] + sys.version_info[1] + sys.version_info[2]

print "Python version --> " + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])

def get_pid(name):
    try:
        return subprocess.check_output(["pidof", name])
    except Exception:
        return "None"

while 1:
    
    p = get_pid(v_process)  # get get_pid() function result
    c = ''
    i = 0

    str = p.split(" ")

    # print str
    # print p.find('None')
    #print str[i]

    if (str[i] != 'None'):        

        while i < len(str):

            if psutil.pid_exists(int(str[i])):                        
                
                proc = psutil.Process(int(str[i]))             

                v_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if p_version >= 21: # python 2.7.12
                    
                    percent = proc.cpu_percent(interval=1)
                                        
                    f_log.write(repr(percent) + "\n")
                    
                else:
                    
                    percent = proc.get_cpu_percent(interval=1)

                    f_log.write(repr(percent) + "\n")

                if percent >= v_consume:

                    proc.kill()
                    
                    f_log.write("kill process |" + repr(v_process) + "|" + repr(v_consume) + "|" + repr(v_time) +  "\n")
                    
                    command = ['service',v_service,'restart'];

                    subprocess.call(command, shell=False)
                                        
                    f_log.write("service restart |" + repr(v_service) + "|" + repr(v_process) + "|" + repr(v_consume) + "|" + repr(proc.pid) + "|" + repr(v_time) + "\n")

            f_log.flush()

            i = i + 1  