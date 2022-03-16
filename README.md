**Programming Assignment 1 HTTP Client/Server**<br>
*Project Statement*<br>
The program will transfer files from a server to the client(s) 
concurrently using TCP connection and threading.
Usage
In order to properly run this program you will need to run the server first with the port number you would like to use as the only argument
(i.e) python3 TCPServer.py 8000 #This will run the server on port 8000
Next run the Client with the arguments as follows:
  python3 TCPClient.py "http://IP[:PORT]/PATH"
So an example of running the client correctly would be:
  python3 TCPClient.py http://127.0.0.1:8000/directory/file
NOTE: it should be known that if no port number is specified (http://IP/PATH) the program will automatically assign port 80.
