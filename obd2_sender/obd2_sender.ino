
uint8_t MSGCAN1[13];
uint8_t MSGCAN2[13];
bool juan = 0;
int ii = 0;
void setup(){
  Serial.begin(115200);
  MSGCAN1[0] = 0x7;
  MSGCAN1[1] = 0xE8;
  MSGCAN1[2] = 0x08;//dlc
  MSGCAN1[3] = 0x41;
  MSGCAN1[4] = 0x10;//id1 MAF
  MSGCAN1[5] = 0x100;//A1
  MSGCAN1[6] = 0x128;//B1
  MSGCAN1[7] = 0x44;//id2 lambda
  MSGCAN1[8] = 116;//A2
  MSGCAN1[9] = 128;//B2
  MSGCAN1[10] = millis();
  MSGCAN1[11] = 13;
  MSGCAN1[12] = 10;

  MSGCAN2[0] = 0x7;
  MSGCAN2[1] = 0xE8;
  MSGCAN2[2] = 0x08;//dlc
  MSGCAN2[3] = 0x41;
  MSGCAN2[4] = 0x0C;//id1 RPM
  MSGCAN2[5] = 0;//A1
  MSGCAN2[6] = 0;//B1
  MSGCAN2[7] = 0x5E;//id2 EFR
  MSGCAN2[8] = 0x02;//A2
  MSGCAN2[9] = 250;//B2
  MSGCAN2[10] = millis();
  MSGCAN2[11] = 13;
  MSGCAN2[12] = 10;

}


void loop(){

  if(juan){
    //MSGCAN1[5] += 0;
    MSGCAN1[6] ++;
    MSGCAN1[9] += ii;

    //MSGCAN2[5] += ii;
    MSGCAN2[6] ++;
    //MSGCAN2[8] += ii;
    //MSGCAN2[9] ++;
    ii++;
    if(ii>20){
      juan = 0;
      ii = 0;
    }
  }else{
    //MSGCAN1[5] -= ii;
    //MSGCAN1[6] -= 2*ii;
    //MSGCAN1[9] -= ii;

    //MSGCAN2[5] -= ii;
    //MSGCAN2[6] -= 2*ii;
    //MSGCAN2[8] -= ii;
    //MSGCAN2[9] -= ii;
    //ii++;
    if(ii>20){
      juan = 1;
      ii = 0;
    }
  }

  MSGCAN1[10] = millis();
  Serial.write(MSGCAN1,13);
  delay(10);
  MSGCAN2[10] = millis();
  Serial.write(MSGCAN2,13);
  delay(10);
}
