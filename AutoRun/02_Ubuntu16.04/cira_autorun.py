import os
from urllib import unquote
from subprocess import Popen
import time


print('###########  CiRA Autorun ############')
import getpass
username = getpass.getuser()
print('user : ', username)


time.sleep(3)


# 1 run ros core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && roscore'])
time.sleep(3)

# 2 run serial_commu
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && source ~/robot_ws/devel/setup.bash --extend && roslaunch serial_commu serial_commu.launch serial_port_name:="/dev/ttyACM1"  ;$SHELL'])
time.sleep(3)

# 2 run rtsp
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && source ~/robot_ws/devel/setup.bash --extend && roslaunch rtsp_cam rtsp_cam.launch rtsp_url1:="rtsp://192.168.1.3/live/ch00_0" rtsp_url2:="rtsp://192.168.1.3/live/ch00_0"  ;$SHELL'])
time.sleep(3)

# 5 schedule reboot
#Popen(["gnome-terminal", '-x' , 'bash', '-c' ,' python ~/cira_startup/schedule_reboot.py'])
#time.sleep(2)

import subprocess
import shlex
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

# 6 run cira core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/kinetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && source ~/robots_ws/devel/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib && while true; do rosrun cira_core_robot cira_core_robot_run _selected:=true _file:=\'/home/wutthikorn/as.npj\' _hide_toolbar:=true _fullscreen:=true; sleep 2s; done ;$SHELL'])
time.sleep(2)
print('####### END #######')
