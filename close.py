import serial

serialPort = serial.Serial(port = "COM4", baudrate=115200, bytesize=8, timeout=10)
serialPort.close()
