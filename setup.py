import os
os.system('cp ~/Spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer')
os.system('dos2unix /data/data/com.termux/files/usr/bin/spammer')
os.system('chmod 777 /data/data/com.termux/files/usr/bin/spammer')
os.system('chmod -R 777 ~/spammer')
os.system('spammer')
