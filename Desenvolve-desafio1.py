import subprocess
subprocess.run(["sudo","apt","update","-y"])
subprocess.run(["sudo","mkdir","-p","/home/je/backup_teste/"])
subprocess.run(["sudo","rsync", "-a", "/home/je/.","/home/je/backup_teste/"])
