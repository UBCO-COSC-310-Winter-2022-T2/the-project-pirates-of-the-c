import unittest
import random
import time
import PIDcontroller


def run_control_loop():
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

class TestControlLoop(unittest.TestCase):
    def test_control_loop(self):
        # This test just checks if the function runs without errors
        run_control_loop()

if __name__ == '__main__':
    unittest.main()
