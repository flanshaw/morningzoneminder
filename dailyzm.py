# zmconcat is at https://github.com/flanshaw/PostboxAlerting/blob/main/zmconcat.py
from zmconcat import new_zmmovie, cleanfolder
import time
from datetime import timedelta
import datetime
import subprocess
import logging
import requests

cleanfolder()
logging.basicConfig(filename='/home/xxxxxx/dailyzm.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.info("creating movie")
today_date = datetime.datetime.now().strftime('%Y-%m-%d')
today_time = datetime.datetime.now().strftime('%H:%M:%S')
yest_date = (datetime.datetime.now() - timedelta(hours = 8)).strftime('%Y-%m-%d')
yest_time = (datetime.datetime.now() - timedelta(hours = 8)).strftime('%H:%M:%S')
logging.info("running new_zmovie %s %s",today_time,yest_time)
file_name = new_zmmovie(yest_date,yest_time,today_date,today_time,1)
logging.info("movie file_name= %s",file_name)
router_external_ip = "xxxxxxxx duckdns.org"
logging.info("external ip = %s", router_external_ip)
mutt_cmd = 'echo http://'+ router_external_ip +':8123/local/' + file_name + ' | mutt -s "Last nights video" xxxxx@gmail.com'
logging.info("mutt cmd= %s", mutt_cmd)
a = subprocess.Popen(mutt_cmd, shell=True)
a.communicate()
logging.info(" email sent, all done, now cleaning up....")
print("....all done.. cleaning up")
cleanfolder()
