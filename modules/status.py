import os
import urllib.request

def get_status(host):
    if host.lower() == 'mcserver':
        host = 'mc.itsjoeoui.com'
        return os.system("ping -c 1 " + host) == 0
    if host.lower() == 'omnivox':
        host = 'https://dawsoncollege.omnivox.ca'
    if host.lower() == 'moodle':
        host = 'https://moodle.dawsoncollege.qc.ca'
    try: 
        return urllib.request.urlopen(host).getcode() == 200
    except:
        return False
