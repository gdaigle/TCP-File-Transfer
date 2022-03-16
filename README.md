# Programming Assignment 1 HTTP Client/Server<br>
Grant Daigle<br>
Dr. Singh<br>
CSCI 4345 Computer Networking<br>
March 16, 2022<br>
## Project Statement<br>
### The program will transfer files from a server to connected client(s) concurrently using TCP connection and threading.<br>
## Installation<br>
   You need python package tqdm before running for the progress bar<br>
   Type ```pip install tqdm``` into terminal/cmd
## Usage<br>
### Server:<br>
In order to properly run this program you will need to run the server first with the port number you would like to use as the only argument<br>
(i.e) python3 TCPServer.py 8000 #This will run the server on port 8000<br>
### Client:<br>
Next run the Client with the arguments as follows:<br>
 python3 TCPClient.py http://ip[:port]/path<br>
So an example of running the client correctly would be:<br>
  python3 TCPClient.py http://127.0.0.1:8000/directory/file<br>
## NOTE: it should be known that if no port number is specified (http://ip/path) the program will automatically assign port 80.<br>
## How it works: <br>
The program works by using a socket connection to connect the client and the server. The client sends a GET message to the server in the format of <br>
GET [path] http/[version]<br>
Once the server receives this GET message from the client the server makes sure the http version is the same as the clients<br>
If the version of the client does not match the server it will send the client<br>
#### http error 505: http version not supported<br>
Once the http version is verified the server will ensure the client sent a GET message. <br>
If the server did not receive a GET message it will send the client<br>
#### http error 400: bad request<br>
Once the GET request has been processed the server will check the filepath provided<br>
The server will either send the client<br>
#### 1). http error 404 file not found
#### 2). http 200 OK
If the server sends the 200 OK response the server will also open the file and read the file bytes and send the bytes to the client<br>
The client will receive the bytes and write them to a file named output.
