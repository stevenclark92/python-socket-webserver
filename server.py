#Import socket module
import socket

#Set host to localhost & port to 8080 (80 for production)
host = ''
port = 8888

#Define server settings - the following can be used in place of certain aspects:
#IPV4 = AF_INET | IPV6 = AF_INET6
#SOCK_STREAM = TCP Byte Stream (ignore others for now)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Socket options - in format (level, option, value)
#SOL_SOCKET is for socket-level ops. Others vary - read the unix docs.
#SO_REUSEADDR reuses the socket address
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind the host & port defined above to the server
serv.bind((host, port))

#Listen for connections
serv.listen(1)

#A while loop to check for connections
while 1:
	#Accept incoming requests
	client, (c_host, c_port) = serv.accept()
	request = client.recv(4096)
	print("Connection received from ", c_host, c_port)
	print(client)
	#Watch syntax here.
	http_response = """HTTP/1.0 200 OK\n"""
	client.send(http_response)

	#Send data - this is just some junk markup
	html_data = """
        <html>
        <head>
        <title>My First Webserver</title>
        </head>
        <body>
        <h1>This is the data to be sent</h1>
        <p>If you can read this, it's working!</p>
        </body>
        </html>
    """
	client.send(html_data)

	#Close the connection
	client.close()