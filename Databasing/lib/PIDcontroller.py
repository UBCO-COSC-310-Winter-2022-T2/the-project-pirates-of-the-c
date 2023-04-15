import time
import random

class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp #define PID values 
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint # reference point entered by user
        
        self.last_error = 0 #initial error values
        self.integral_error = 0
        
        t = time.time() 
        self.last_time = t
        # print(t)
        
    

        
    def update(self, current_value):
        error = self.setpoint - current_value
        
        t1 = time.time()
        current_time = t1
        # print(t1)
        delta_time = current_time - self.last_time
        # print(delta_time)
        
        derivative_error = (error - self.last_error) / delta_time
        self.integral_error += error * delta_time
        
        output = self.kp * error + self.ki * self.integral_error + self.kd * derivative_error #gives an output that will adjust the current system output to achieve reference
        
        self.last_error = error
        self.last_time = current_time
        
        return output

kp = 1.0
ki = 0.1
kd = 0.01
    # Set the setpoint and initialize the PID controller
setpoint = 50
pid = PIDController(kp, ki, kd, setpoint)

    # Run the control loop
count = 0
while True:
        # Simulate the current temperature
        current_temperature = random.uniform(0, 100)

        # Update the PID controller
        output = pid.update(current_temperature)

        # Print the current temperature and PID output
        print(f"Temperature: {current_temperature:.2f}  Output: {output:.2f}")

        time.sleep(1)

        count +=1

        if count == 10:
             break
        


