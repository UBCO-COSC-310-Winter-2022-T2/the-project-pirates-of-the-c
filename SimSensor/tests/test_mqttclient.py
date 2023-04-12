import unittest
from SimSensor.simsensor import * # From in the SimSensor folder and the simsensor python file import all the functions within
from random import Random

# Not sure if these tests are sufficient but I'll roll with it for now

class test_brokerconnect(unittest.TestCase):
    def test_createclient(self):  # Test the creation of a mqtt client
       client = simsensor.createclient()
       self.assertIsInstance(client, mqtt.Client)
       
    def test_connection(self): # Test the connection of a mqtt client to a broker
        client = simsensor.createclient()  # Needs the create client function to work first
        simsensor.brokerconnect(client)
        self.assertTrue(client.is_connected()) # Connect sucessful
        simsensor.brokerdisconnect(client)
        self.assertFalse(client.is_connected()) # Disconnect sucessful
        
    def test_publishmessage(self):
        client = simsensor.createclient()
        simsensor.brokerconnect(client)
        topic = "test/topic"
        payload = "test message"
        client.publish(topic, payload)
        simsensor.brokerdisconnect(client)
        self.assertTrue(True) # Sucessfully published a message without exceptions