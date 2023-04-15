import random
import time
import bandpassfilter
import PIDcontroller
import numpy as np


x = np.linspace(0, 10 * np.pi, num=600)
n = np.random.normal(scale=8, size=x.size)
y = 100 * (np.sin(x) + np.sin(10*x))+ n
fil = bbfilter(y,1000,20,70)
current_temperature = 0.005*fil


kp = 1.0
ki = 0.1
kd = 0.01

# Set the setpoint and initialize the PID controller
setpoint = 50
pid = PIDController(kp, ki, kd, setpoint)

while True:
        

        # Update the PID controller
        output = pid.update(current_temperature)

        # Print the current temperature and PID output
        print(f"Temperature: {current_temperature:.2f}  Output: {output:.2f}")

        time.sleep(1)