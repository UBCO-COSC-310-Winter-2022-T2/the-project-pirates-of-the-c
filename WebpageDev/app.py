import time
from flask import Flask, jsonify, render_template
import random
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Define MQTT client parameters
mqtt_broker_host = "localhost" # replace with proper parameters
mqtt_broker_port = 1883 # replace with proper parameters
mqtt_topic = "temperature" # replace with proper parameters

# Create MQTT client instance
#mqtt_client = mqtt.Client()

# Define callback functions
def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode("utf-8"))

# Set callback functions
#mqtt_client.on_connect = on_connect
#mqtt_client.on_message = on_message

# Connect to MQTT broker
#mqtt_client.connect(mqtt_broker_host, mqtt_broker_port)


def check_temperature():
    # Start the MQTT client loop to listen for incoming messages
    mqtt_client.loop_start()

    # Publish a message to trigger a temp value
    mqtt_client.publish("temperature", "check")

    # Wait for a message to be received
    time.sleep(1)
    # Stopt loop
    mqtt_client.loop_stop()

    # Return the temperature data
    return temperature

# Generate random temperature data (for testing when not connected to MQTT broker)
def generate_data():
    return random.uniform(70, 80)

# Route to return temperature data as JSON
@app.route('/api/temperature')
def temperature():
    # the following should be replaced by data = get_temp when connected to the broker.
    data = {
        'temperature1': generate_data(),
        'temperature2': generate_data(),
        'temperature3': generate_data()
    }
    return jsonify(data)


# Route to render HTML template that displays temperature data
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
