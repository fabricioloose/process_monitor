#!/usr/bin/python

"""
Compile bytecode:
pycompile process2.py

*English
Verify if the process /etc/init.d/process what control the winbind snap 
it is stop or no.
Case yes execute this is verified every minutes
Remember what only one process python should be running

*Portuguese
Verifica se o processo /etc/init/process que contrala se o winbind estourou
esta parado ou nao.
Caso esteja executa executa
verifica a cada minito
Lembrar que somente um processo python deve estar rodando

schedule crontab example
*/1 * * * * ( sudo /usr/bin/python /root/process_cron.py ) >/dev/null2>&1
"""

import os
import string
import subprocess
import sys
import datetime
import psutil

v_process = "python"
v_psutilversion = 3

def get_pid(name):
    try:
        return subprocess.check_output(["pidof", name])
    except Exception:
        return "None"
    
p = get_pid(v_process)  # get get_pid() function result

str = p.split(" ")

print str
print len(str)

"""
Checking if one process python be execution.
if you are is signal what process.py be stoped, then initialize

Checando se somente um processo python esta em execucao
se estiver eh sinal que o process process.py esta parado,
entao inicializa
"""
if ( len(str) == 1 ):
    os.system("/etc/init.d/process start")

# Checking if the winbind be stoped, you are initialize
# Checando se o winbindd esta parado, se estiver inicializa

p = get_pid("winbindd")

str = p.split(" ")

print str
print len(str)

if ( len(str) == 1 ):
    os.system("/etc/init.d/winbind restart")