 
#
# Copyright 2024 Leon Lum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import paho.mqtt.client as paho
from paho import mqtt

import ssl
import paho.mqtt.publish as publish
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 


class Pahomqtt:

    # using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
    # userdata is user defined data of any type, updated by user_data_set()
    # client_id is the given name of the client
    client = paho.Client(paho.CallbackAPIVersion.VERSION2,
                            client_id="", 
                            userdata=None, 
                            protocol=paho.MQTTv5,
                            transport='websockets' )
    
    # enable TLS for secure connection
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    # set username and password
    username =''
    password=''
    mqtt_server =''
    client.username_pw_set(username, passwd)
    # connect to Mqtt Server on port 8883 (default for MQTT)
    client.connect(mqtt_server, 8883)

    properties=Properties(PacketTypes.PUBLISH)
    properties.MessageExpiryInterval=45 # in seconds



 # constructor function    
    def __init__(self):
 #         self.client = client
 #         self.properties = properties
 # setting callbacks, use separate functions like above for better visibility
      
        self.client.on_connect  = self.on_connect
        self.client.on_subscribe  = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_publish  = self.on_publish
        properties = self.properties

        self.client.loop_start()
       
    # subscribe to all topics of encyclopedia by using the wildcard "#"
        # client.subscribe("#topic/dew_data", qos=1)


    # a single publish, this can also be done in loops, etc.
    # client.publish("#topic/dew_data", payload="hot", qos=1, properties=properties) 
    # client.subscribe('common', options=SubscribeOptions(noLocal=True))
    

    # time.sleep(10)  # wait
    # client.loop_stop()  # stop the loop


    # loop_forever for simplicity, here you need to stop the loop manually
    # you can also use loop_start and loop_stop
    # client.loop_forever()
    # payload_one ='{"type": "new", "data"}'
    # client.publish("#topic/dew_data", payload=payload_one, qos=1, properties=properties)


    # setting callbacks for different events to see if it works, print the message etc.
    def on_connect(self, client, userdata, flags, rc, properties=None):
        """
            Prints the result of the connection with a reasoncode to stdout ( used as callback for connect )

            :param client: the client itself
            :param userdata: userdata is set when initiating the client, here it is userdata=None
            :param flags: these are response flags sent by the broker
            :param rc: stands for reasonCode, which is a code for the connection result
            :param properties: can be used in MQTTv5, but is optional  
    
        """
        print("CONNACK received with code %s." % rc)


    # with this callback you can see if your publish was successful
    def on_publish(self, client, userdata, mid, granted_qos, properties=None):
        """
            Prints mid to stdout to reassure a successful publish ( used as callback for publish )
            :param client: the client itself
            :param userdata: userdata is set when initiating the client, here it is userdata=None
            :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
            :param granted_qos: this is the qos that you declare when subscribing, use the same one for publishing
            :param properties: can be used in MQTTv5, but is optional
        """
        # self.client.disconnect()
        print("mid: " + str(mid))


    # print which topic was subscribed to
    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        """
            Prints a reassurance for successfully subscribing

            :param client: the client itself
            :param userdata: userdata is set when initiating the client, here it is userdata=None
            :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
            :param granted_qos: this is the qos that you declare when subscribing, use the same one for publishing
            :param properties: can be used in MQTTv5, but is optional
        """
        print("Subscribed: " + str(mid) + " " + str(granted_qos))


    # print message, useful for checking if it was successful
    def on_message(self, client, userdata, msg):
        """
            Prints a mqtt message to stdout ( used as callback for subscribe )

            :param client: the client itself
            :param userdata: userdata is set when initiating the client, here it is userdata=None
            :param msg: the message with topic and payload
        """
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def connect_callback(self, client, userdata, connect_flags, reason_code, properties):

        print(f"connect callback  {reason_code}.")

