import os
from urllib import unquote
from subprocess import Popen
import time

serial_port_name = "/dev/ttyACM0"
rtsp_url1 = "rtsp://192.168.1.3/live/ch00_0"
rtsp_url2 = "rtsp://192.168.1.4/live/ch00_0"
cira_core_path = "/home/tdem/Desktop/Test_park.npj"
full_screen = 'false'

print('###########  CiRA Autorun ############')
import getpass
username = getpass.getuser()
print('user : ', username)


time.sleep(3)


# 1 run ros core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && roscore'])
time.sleep(3)

# 2 run serial_commu
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && source ~/catkin_ws/devel/setup.bash --extend && roslaunch serial_commu serial_commu.launch serial_port_name:=%s  ;$SHELL'%serial_port_name])
time.sleep(3)

# 3 run rtsp
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/kinetic/setup.bash && source ~/catkin_ws/devel/setup.bash --extend && roslaunch rtsp_cam rtsp_cam.launch rtsp_url1:=%s rtsp_url2:=%s  ;$SHELL'%(rtsp_url1,rtsp_url2)])


# 5 schedule reboot
#Popen(["gnome-terminal", '-x' , 'bash', '-c' ,' python ~/cira_startup/schedule_reboot.py'])
time.sleep(2)

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
time.sleep(3)
# 6 run cira core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && source /opt/ros/kinetic/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && source ~/robot_ws/devel/setup.bash --extend && export LD_LIBRARY_PATH=$(find /usr/lib -iname nvidia-* -type d 2>&1 | sed "{:q;N;s/\\n/:/g;t q}"):${LD_LIBRARY_PATH} && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib && while true; do  rosrun cira_core cira_core_run _selected:=true _file:=%s _hide_toolbar:=true _fullscreen:=%s; sleep 2s; done ;$SHELL'%(cira_core_path,full_screen)])
time.sleep(2)
print('####### END #######')
