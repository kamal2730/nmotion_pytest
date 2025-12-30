from nmotion_transport import *
import time

iface=USBInterface("/dev/ttyACM0")
act1=Actuator(0,iface)

print("\n--- Available Methods for Actuator ---")
# This prints a list of every function you can call on 'act1'
print([method for method in dir(act1) if not method.startswith('_')])

time.sleep(2)
set_status = act1.setPositionControl(180,200)#angle #speed
time.sleep(2)
(get_status, count) = act1.getOutputPosition()
print(f'Encoder count is: {count} status{get_status}')
del act1
iface.close()

