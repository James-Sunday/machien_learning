import serial
import time 


class ArduinoController:
    def __init__(self, port, baudrate):
        self.port =port 
        self.baudrate = baudrate
        self.serial_command=serial.Serial(self.port, self.baudrate)
    def send_command(self, command):
        send_com= self.serial_command.write(command.encode('utf-8'))
        return send_com

    def handshake(self):
        return self.send_command('H')
    
    def wave(self):
        return self.send_command('W')
        
    def all_movement(self):
        return self.send_command('S')

    def nod_head(self):
        return self.send_command('N')
    
    def thinker(self):
        return self.send_command('T')

    def jaw(self):
        return self.send_command('M')

    def left_waist(self):
        return self.send_command('L')

    def right_waist(self):
        return self.send_command('R')
    def wake_up(self):
        return self.send_command('U')

    def default_mode(self):
        return self.send_command('D')

if __name__=="__main__":
    action= ArduinoController('/dev/ttyUSB0', 9600)
    action.wake_up()
    action.handshake()
    action.default_mode()
