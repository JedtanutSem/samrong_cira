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
          * AutoRun
          * samrong
        
### 3. ติดตั้ง Arduino
ปฏิบัติตามขั้นตอนการติดตั้ง [Arduino](https://ubuntu.com/tutorials/install-the-arduino-ide#1-overview)

### 4. เปลี่ยน Permission ของ Arduino Com Port
```console
$ sudo usermod -a -G dialout $USER
การเปลี่ยนแปลงจะมีผลหลังจาก Log Out โปรด Log Out หรือ Restart เครื่อง
```
### 5. จัดการ Code เพื่อเลือก IO ของ Arduino
ไฟล์โค้ดจะอยู่ในโฟลเดอร์ [Arduino_Ser](https://github.com/JedtanutSem/samrong_cira/tree/main/samrong/Arduino_Ser)
* Home
    * catkin_ws
      * build
      * devel 
      * src
        * CMakeLists.txt
        * samrong_cira 
          * CmakeLists.txt
          * README.md
          * AutoRun
          * samrong 
            * cira_core
            * [--Arduino_Ser--]
            * rtsp_cam
            * serial_commu

![Ardui_ser](https://user-images.githubusercontent.com/94428679/155933375-613944cf-bdca-4a5d-ac00-306267734457.png)

เลือก Input Pin และ Output Pin โดยค่าเริ่มต้นจะเป็นดังภาพ

### 6. ตั้งค่าเริ่มต้นโปรแกรมอัตโนมัติเมื่อเปิดเครื่อง
แก้ไขไฟล์ในโฟลเดอร์ Autorun 
* Home
    * catkin_ws
      * build
      * devel 
      * src
        * CMakeLists.txt
        * samrong_cira 
          * CmakeLists.txt
          * README.md
          * [--AutoRun--]
          * samrong   
เลือกโฟลเดอร์ตามเวอร์ชั่น Ubuntu ที่ใช้งาน (16.04, 18.04)

