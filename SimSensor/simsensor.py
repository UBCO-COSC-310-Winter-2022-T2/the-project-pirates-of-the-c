import paho.mqtt.client as mqtt
import random, time, math

def main():
        return

def brokerconnect(client):
        host = 'localhost'
        port = 1883
        keepalive = 60
        client.connect(host, port, keepalive)
        return 

def brokerdisconnect(client):
        return

def createclient():
        client = mqtt.Client(client_id=None, clean_session=True, userdata=None, transport='tcp')
        return client

def numgen():
        current_time = time.localtime()
        minutes_passed = (current_time.tm_hour*60) + current_time.tm_min # The number of minutes passed in the day
        angle = (minutes_passed*2*math.pi) / 1440 # Convert minutes to an angle between 0 and 2pi
        phase = -2*math.cos(angle)+20 # Convert the angle to a sine function between 18 and 22 thoughout the day
        noise = random.randint(950,1050)/1000 # Create a coefficient that scales the phase
        temp = phase * noise # Multiply the phase by the noise to get the final random temp   
        return temp

if __name__ == "__main__":
        main()