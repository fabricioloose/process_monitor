# process_monitor

Set of three files that is intended to monitor the winbind process overflow.

My server had the problem of popping the winbind process, making samba server mappings unavailable.

So I ended up having the idea of creating this application, which checks when winbind pops up and automatically kills the winbindd process, thus preventing the service from being unavailable.


1. process_cron.py

* schedule in cron

2. process_final.py

* Responsible for killing the winbindd process. Put in some place with execution permission.

3. process
init linux (init.d)
