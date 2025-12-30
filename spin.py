from nmotion_transport import *
import time

iface=USBInterface("/dev/ttyACM0")
act1=Actuator(0,iface)
time.sleep(2)
act1.setVelocityControl(361)
time.sleep(2)
(get_status, count) = act1.getOutputPosition()
print(f'Encoder count is: {count} status{get_status}')
del act1
iface.close()

