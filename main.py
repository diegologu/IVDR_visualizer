import serial
import numpy as np

serialPort = serial.Serial(port = "COM4", baudrate=115200, bytesize=8, timeout=10)
f=open('RawData.txt','w')
g=open('CookedData.txt','w')
f.truncate(0)
g.truncate(0)
errores=0
Ta=0
T=0
RPM = 0
MAF = 0
lam = 0
EFR = 0
EFR_2 = 0
val_1 = 0
val_2 = 0

while(1):
    if(serialPort.in_waiting>0):
        serialString = serialPort.read(13)
        serialInt=np.frombuffer(serialString, dtype=np.uint8)
        if(serialInt[11]!=13 and serialInt[12]!=10):
            errores=errores+1
            print(errores)
            bant=0
            while(1):
                b=serialPort.read(1)
                if (bant==13 and b==10):
                    break
                bant=b
        else:
            print(serialInt)
            ID=serialInt[0]*256+serialInt[1]
            f.write(str(ID)+',')
            for i in range(2,10):
                f.write(str(serialInt[i])+',')
            f.write(str(serialInt[10])+'\n')

            Tn=int(serialInt[10])
            dT=Tn-Ta
            if (dT>=0):
              T=T+dT
            else:
              T=T+dT+255
            Ta=Tn

            if(serialInt[4] == 16):
                MAF =(((256*serialInt[5])+serialInt[6])/100)
                lam =(((2/65536)*(256*serialInt[8])+serialInt[9]))
                EFR_2 = MAF/(14.7*lam*680) # L/s
                val_1 = 1
            if(serialInt[4] == 12):
                RPM =(((256*serialInt[5])+serialInt[6])/4)
                EFR =(((256*serialInt[8])+serialInt[9])/20)/3600
                val_2 = 1
            if(val_1 and val_2):
                g.write(str(T/1000)+','+str(RPM)+','+str(EFR)+','+str(EFR_2)+'\n')
                val_1 = 0
                val_2 = 0


serialPort.close()
