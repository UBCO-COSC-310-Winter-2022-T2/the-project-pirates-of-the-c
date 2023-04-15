import paho.mqtt.client as mqtt
import random, time, math, sys, os

#containername = 'sensor1' # For non containerized testing
#broker_address = 'localhost' # For non containerized testing
containername = os.environ.get('containername', 'localhost')
broker_address = os.environ.get('broker_address', 'localhost')
delay = os.environ.get('delay', 'localhost')
broker_port = 1883 # default port
keepalive = 60
stream = containername + 'data' # Topic stream

def main():
        time.sleep(int(delay))
        client = createclient()
        brokerconnect(client)
        try:
                while True:
                        num = f'{numgen():.3f}' # Temp
                        client.publish(stream, num) # Publish to Broker
                        print(f'Publishing --> {num}')
                        time.sleep(5) # Wait 5 sec before sending another
        except KeyboardInterrupt:
                print('Disconnecting from broker')
        client.disconnect()
        return

def on_log(client, userdata, level, buf): # Called every time an event happens
        print(f'MQTT {containername}: {buf}') # Prints the message of the event

def on_connect(client, userdata, flags, rc): # When the client connects this is called
        if rc == 0: 
                print('Connected OK') # Remote connection equals zero, connection was sucessful
        else:
                print('Bad connection returned code= ',rc) # Not sucessful
        
def on_disconnect(client, userdata, flags, rc): # Called when client disconnects from broker
        print(rc)
        print('on_connect')
        
        
def brokerconnect(client):
        if client.connect(broker_address, broker_port, keepalive) != 0: # Returns 0 if client connects
                print("Can't connect to MQTT Broker")
                #sys.exit(-1)
        time.sleep(5) # MUST SLEEP FOR 5 SEC TO LET BROKER PROCESS REQUEST
        return 

def brokerdisconnect(client):
        client.disconnect()
        client.loop_stop()
        return

def createclient():
        client = mqtt.Client(containername)
        client.on_log = on_log
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.loop_start()
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