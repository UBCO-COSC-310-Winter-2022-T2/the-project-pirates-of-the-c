import time
import random

class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        
        self.last_error = 0
        self.integral_error = 0
        
        t = time.time()
        self.last_time = t
        print(t)
        

        
    def update(self, current_value):
        error = self.setpoint - current_value
        
        current_time = time.time()
        delta_time = current_time - self.last_time
        
        derivative_error = (error - self.last_error) / delta_time
        self.integral_error += error * delta_time
        
        output = self.kp * error + self.ki * self.integral_error + self.kd * derivative_error
        
        self.last_error = error
        self.last_time = current_time
        
        return output

# Set the initial gains
kp = 1.0
ki = 0.1
kd = 0.01

# Set the setpoint and initialize the PID controller
setpoint = 50
pid = PIDController(kp, ki, kd, setpoint)

# Run the control loop
while True:
    # Simulate the current temperature
    current_temperature = random.uniform(0, 100)
    
    # Update the PID controller
    output = pid.update(current_temperature)
    
    # Print the current temperature and PID output
    print(f"Temperature: {current_temperature:.2f}  Output: {output:.2f}")
    
    time.sleep(1)
