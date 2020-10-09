from dan_socket.client import DanClient

client = DanClient("127.0.0.1", 5050)

@client.event("on_message")
def message_received(message):
    print("Received from Server: {}".format(message))

@client.event("on_connection_closed")
def client_closed():
    print("Server disconnected")

client.start()

