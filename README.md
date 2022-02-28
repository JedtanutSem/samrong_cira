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



เลือกโฟลเดอร์ตามเวอร์ชั่น Ubuntu ที่ใช้งาน (16.04, 18.04) และเข้าไปแก้ไขในไฟล์ cira_autorun.py จะมีตัวแปร 
* rtsp_url1 (ที่อยู่ url ของกล้องตัวที่ 1)
* rtsp_url2 (ที่อยู่ url ของกล้องตัวที่ 2)
* serial_port_name (ชื่อ com port ของ Arduino สามารถตรวจสอบได้จากโปรแกรม Arduino ที่ได้ติดตั้งในขั้นตอนที่ 3)
* cira_core_path  (ที่อยู่ของไฟล์ .npj [ไฟล์โปรเจค] cira core) 
 
ให้แก้ไขให้ตรงกับหน้างานที่ใช้งานโดยจะมีค่า Default ดังนี้

* rtsp_url1        = "rtsp://192.168.1.3/live/ch00_0"
* rtsp_url2        = "rtsp://192.168.1.4/live/ch00_0"
* serial_port_name = "/dev/ttyACM0"
* cira_core_path = "/home/tdem/Desktop/Test_park.npj" (สามารถคลิ๊กขวาที่ไฟล์โปรเจคและเลือก properties จะได้ path อยู่ในหัวข้อ Location)
* full_screen = 'false'

#### 6.1 ทดสอบความการใช้งานเบื้องต้นของการเริ่มทำงาน Autorun

```console
$ cd ~/catkin_ws/src/AutoRun/<ชื่อโฟลเดอร์ Ubuntu ที่ใช้งาน>
ตัวอย่าง : $ cd ~/catkin_ws/src/AutoRun/02_Ubuntu16.04
$ python cira_autorun.py
```
หากโปรแกรมเริ่มขึ้นมาโดยอัตโนมัติจึงดำเนินการขั้นตอนต่อไปได้ หากไม่ได้ให้ตรวจสอบตัวแปรข้างต้นที่กล่าวมาอีกครั้ง หากยังพบปัญหาสามารถติดต่อกลับเพื่อแก้ปัญหา

#### 6.2 ตั้งค่าการเริ่มต้นอัตโนมัติเมื่อเปิดเครื่อง
เปิดหน้าแสดงโปรแกรมทั้งหมดใน Ubuntu อาจเรียกว่า Search your computer หรือ Show application (ขึ้นอยู่กับเวอร์ชันของ Ubuntu) แล้วเรียกหา Startup Applications Preferences จะได้หน้าต่างดังภาพ 
![Startup_APP](https://user-images.githubusercontent.com/94428679/155946323-26395d51-0632-4c0d-b8e3-bd28cdb73b4f.png)
* เลือก Add เพื่อเพิ่มโปรแกรมที่ต้องการจะให้เริ่มต้นเมื่อเปิดเครื่อง
![Add_startup](https://user-images.githubusercontent.com/94428679/155946614-9394a9bf-f27c-4496-98ab-7ea12d28ec8d.png)
* Name : ตั้งชื่อตามสะดวก
* Command : gnome-terminal -e 'python 'home/<ชื่อเครื่อง>/catkin_ws/src/samrong_cira/AutoRun/<ชื่อ Folder เวอร์ชั่นของ Ubuntu ที่ใช้งาน>/cira_autorun.py''
* Comment : สามารถ comment ได้ตามสะดวก


ตัวอย่าง gnome-terminal -e 'python 'home/tdem/catkin_ws/src/samrong_cira/AutoRun/02_Ubuntu16.04/cira_autorun.py'' (สามารถคลิ๊กขวาที่ไฟล์ cira_autorun.py และเลือก properties จะได้ path อยู่ในหัวข้อ Location)

เมื่อตั้งค่าเรียบร้อยให้กด Add และปิดหน้าต่าง Startup Applications Preferences


### 7. ตั้งค่า Schedule Reboot

* เปิด Terminal
```console
$ sudo apt-get update
$ sudo apt-get install nano
$ sudo nano /etc/crontab
```
เมื่อรันคำสั่งจะได้หน้าต่างดังภาพ
![crontab](https://user-images.githubusercontent.com/94428679/155951778-b5f3510e-3dc4-4b32-b5a2-237dda4ff598.png)

ให้ใส่ข้อความนี้ลงไปที่บรรทัดสุดท้าย โดยการใช้ปุ่มลูกศรเลื่อนเคอร์เซอร์ลงไปที่บรรทัดสุดท้าย  
00 12 * * * root reboot (คอมพิวเตอร์จะ Reboot ทุก 12.00 น.) ดังภาพ
![Screenshot from 2022-02-28 03-48-38](https://user-images.githubusercontent.com/94428679/155952855-4a55ac50-0036-4944-9613-653c3cbc7e57.png)

เมื่อดำเนินการเรียบร้อยให้กด ctrl+o และ enter และ ctrl+x  
ข้อมูลเพิ่มเติมในการตั้งค่าวันและเวลาสามารถอ่านได้ [ที่นี่](https://linuxhint.com/schedule-reboot-daily-linux/)

## จากนั้น Restart เครื่องและตรวจสอบการทำงานของ Autorun  Schedule Reboot จะเริ่มทำงานหลังจาก Restart เครื่อง

