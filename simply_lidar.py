import time
from adafruit_servokit import ServoKit
import time
import VL53L0X
import matplotlib.pyplot as plt

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()
# fig = plt.figure()

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_GOOD_ACCURACY_MODE)
x= []
y=[]

kit = ServoKit(channels=8)
for i in range(180,0,-1):
        kit.servo[0].angle = i
        distance = tof.get_distance()
#         if (distance > 0):
#             print ("%d mm, %d" % (distance, 180-i))
        x.append(180-i)
        y.append(distance)
        
        #time.sleep(0.001)

plt.scatter(x,y)
plt.show()
