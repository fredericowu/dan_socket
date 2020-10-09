# Adding the library path.
# TEST PURPOSE ONLY
#import sys
#import os
#sys.path.append("{}/../dan_socket".format(os.getcwd()))
##########################
from dan_socket.server import DanServer


server = DanServer("127.0.0.1", 5050)

@server.event("on_message")
def message_received(client, message):
    print("Client {}: {}".format(client, message))

@server.event("on_new_connection")
def new_connection(client):
    print("[NEW] Client {}".format(client))
    client.send("HI\r\n")
    
@server.event("on_connection_closed")
def client_closed(client):
    print("[CLOSED] Client {}".format(client))


server.start()

