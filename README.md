# Morning ZM video
Every morning at 6:45 (crontab) runs python script to combine all last nights zoneminder alarms into one OUTPUT.mp4, moves it into hassio, and sends email with url to the file.

very handy over breakfast to see what happend last night

# crontab

45 06 * * * /usr/bin/python3 /home/xxx/dailyzm.py

