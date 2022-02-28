#include <SoftwareSerial.h>

int out1_pin =12;
int out2_pin =3;
int out3_pin =4;
int out4_pin =5;
int out5_pin =6;
int out6_pin =7;

int in1_pin =8;
int in2_pin =9;
int in3_pin =10;
int in4_pin =11;
int in5_pin =22;
int in6_pin =24;

String read_str;

String out1_str;
String out2_str;
String out3_str;
String out4_str;
String out5_str;
String out6_str;

int out1_int=0;
int out2_int=0;
int out3_int=0;
int out4_int=0;
int out5_int=0;
int out6_int=0;




void setup() 
{

  Serial.begin(9600);
  pinMode(out1_pin,OUTPUT);
  pinMode(out2_pin,OUTPUT);
  pinMode(out3_pin,OUTPUT);
  pinMode(out4_pin,OUTPUT);
  pinMode(out5_pin,OUTPUT);
  pinMode(out6_pin,OUTPUT);
  pinMode(in1_pin,INPUT_PULLUP);
  pinMode(in2_pin,INPUT_PULLUP);
  pinMode(in3_pin,INPUT_PULLUP);
  pinMode(in4_pin,INPUT_PULLUP);
  pinMode(in5_pin,INPUT_PULLUP);
  pinMode(in6_pin,INPUT_PULLUP);
}

void loop() {
  if(Serial.available()>0) {
    out1_str = Serial.readStringUntil(',');
    out2_str = Serial.readStringUntil(',');
    out3_str = Serial.readStringUntil(',');
    out4_str = Serial.readStringUntil(',');
    out5_str = Serial.readStringUntil(',');
    out6_str = Serial.readStringUntil(',');

    out1_int = out1_str.toInt();
    out2_int = out2_str.toInt();
    out3_int = out3_str.toInt();
    out4_int = out4_str.toInt();
    out5_int = out5_str.toInt();
    out6_int = out5_str.toInt();

    digitalWrite(out1_pin, out1_int);
    digitalWrite(out2_pin, out2_int);
    digitalWrite(out3_pin, out3_int);
    digitalWrite(out4_pin, out4_int);
    digitalWrite(out5_pin, out5_int);
    digitalWrite(out6_pin, out6_int);
    
    Serial.print(digitalRead(in1_pin));
    Serial.print(",");
    Serial.print(digitalRead(in2_pin));
    Serial.print(",");
    Serial.print(digitalRead(in3_pin));
    Serial.print(",");
    Serial.print(digitalRead(in4_pin));
    Serial.print(",");
    Serial.print(digitalRead(in5_pin));
    Serial.print(",");
    Serial.print(digitalRead(in6_pin));
    Serial.println("");


  }
}
 
