# CiRA CORE Serial and RTSP Camera Autorun
โปรดปฏิบัติตามขั้นตอนและเชื่อมต่ออินเทอร์เน็ตขณะติดตั้ง
## อุปกรณ์ที่จำเป็น
1. Arduino Mega
2. RTSP Camera
3. PC Computer
### 1. สร้าง Workspace สำหรับ ROS CORE
รายละเอียดเพิ่มเติมได้ที่ [ROS Tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
```console
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
### 2. ดาวน์โหลด Package
```console
$ cd ~/catkin_ws/src
$ git clone https://github.com/JedtanutSem/samrong_cira.git
$ cd ~/catkin_ws/
$ catkin_make
```
โปรดตรวจสอบโฟลเดอร์ต้องปรากฏดังนี้
  * Home
    * catkin_ws
      * build
      * devel 
      * src
        * CMakeLists.txt
        * samrong_cira 
          * CmakeLists.txt
          * README.md
          * samrong 
            * cira_core
            * rtsp_cam
            * serial_commu
### 3. ติดตั้ง Arduino
ปฏิบัติตามขั้นตอนการติดตั้ง [Arduino](https://ubuntu.com/tutorials/install-the-arduino-ide#1-overview)

### 4. เปลี่ยน Permission ของ Arduino Com Port
```console
$ sudo usermod -a -G dialout $USER
การเปลี่ยนแปลงจะมีผลหลังจาก Log Out โปรด Log Out หรือ Restart เครื่อง
```
### 5. จัดการ Code เพื่อเลือก IO ของ Arduino
