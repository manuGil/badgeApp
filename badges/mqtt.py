import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("workshop/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="maker", password="OpenSciFest#2021")

client.connect("testbed.dcc.tudelft.nl", 443, 60)

# Blocking call that processes network traffic
client.loop_forever()

# TODO: CONFIGURATION ON BADGE CLIENT
# host: testbed.dcc.tudelft.nl
# port: 8080
# username: maker
# password:
# topic: workshop/<badgename>

# MESSAGE:
# {"name": "<badgename>", "color": RGB/HEX?}

# TODO: IMPORTANT
# Badgenames must be unique

# Message format:
# b'{"name":"default_name","color":[214,221,220]}'

# "{\"name\":\"default_name\",\"color\":[214,221,220]}"

