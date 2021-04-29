import smbus
import time
class Adc2:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.ADDRESS= 0x48
        self.PCF8591_CMD=0x40 
        self.ADS7830_CMD= 0x84
        
        for i in range(3):
            aa=self.bus.read_byte_data(self.ADDRESS,0xf4)
            if aa < 150:
                self.Index="PCF8591"
            else:
                self.Index="ADS7830" 
    def analogReadPCF8591(self,chn):
        value=[0,0,0,0,0,0,0,0,0]
        for i in range(9):
            value[i] = self.bus.read_byte_data(self.ADDRESS,self.PCF8591_CMD+chn)
        value=sorted(value)
        return value[4]   
        
    def analogWritePCF8591(self,value):
        self.bus.write_byte_data(self.ADDRESS,cmd,value)
        
    def recvPCF8591(self,channel):
        while(1):
            value1 = self.analogReadPCF8591(channel)
            value2 = self.analogReadPCF8591(channel)
            if value1==value2:
                break;
        voltage = value1 / 256.0 * 3.3  #calculate the voltage value
        voltage = round(voltage,2)
        return voltage
    def recvADS7830(self,channel):
        COMMAND_SET = self.ADS7830_CMD | ((((channel<<2)|(channel>>1))&0x07)<<4)
        self.bus.write_byte(self.ADDRESS,COMMAND_SET)
        while(1):
            value1 = self.bus.read_byte(self.ADDRESS)
            value2 = self.bus.read_byte(self.ADDRESS)
            if value1==value2:
                break;
        voltage = value1 / 255.0 * 3.3  #calculate the voltage value
        voltage = round(voltage,2)
        return voltage
        
    def recvADC(self,channel):
        if self.Index=="PCF8591":
            data=self.recvPCF8591(channel)
        elif self.Index=="ADS7830":
            data=self.recvADS7830(channel)
        return data
    def i2cClose(self):
        self.bus.close()
