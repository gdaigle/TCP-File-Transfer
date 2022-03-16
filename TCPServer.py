from socket import *
import os
import sys
import threading
#Constants
FORMAT = "utf-8"
SIZE = 8192
def connected_clients(connectionSocket, addr):
    print("[+] Accepted connection from ", addr)
    requests = connectionSocket.recv(1024).decode(FORMAT)
    #Splits the HTTP Request into ["GET", "<FILEPATH>", "HTTP/<Version>\r\n\r\n"]
    requests = requests.split(" ")
    #If the http version is 1.1
    if("1.1" in requests[2]):
        #If requests[0] is equal to GET
        if(requests[0] == "GET"):
            #Intializing the variable the_file_path and removing the first /
            the_file_path = requests[1].replace("/", "", 1)
            #If the file path exists
            if(os.path.exists(the_file_path)):
                #Send http response 200 OK to the client
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode(FORMAT))
                #open the file path 
                with open(the_file_path, "rb") as file:
                    #read the file and send to the client
                    read_file = file.read(SIZE)
                    while True:
                        if(not read_file):
                            break
                        else:
                            connectionSocket.sendall(read_file) 
                            read_file = file.read(SIZE)
            #If the file path does not exist
            elif(not os.path.exists(the_file_path)):
                #Send http response 404 File Not Found to the client
                connectionSocket.send("HTTP/1.1 404 File Not Found\r\n\r\n".encode(FORMAT))
        #If requests[0] is not equal to GET
        else:
            #Send http response 400 Bad Request to the client
            connectionSocket.send("HTTP/1.1 400 Bad Request\r\n\r\n".encode(FORMAT))
    #If the http version is not 1,1
    else:
        #Send http response 505 HTTP Version Not Supported to the client
        connectionSocket.send(" ","505 HTTP Version Not Supported\r\n\r\n".encode(FORMAT))
    #Close the socket connection
    connectionSocket.close()

def start_server():
    #if the command line argument does not equal 1
    if(not sys.argv == 1):
        print("Usage: python3 TCPServer.py <port>")
        sys.exit(1)
    else:
        #gets the server port number from command line argument
        serverPort = int(sys.argv[1])
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print("[LISTENING] The server is listening and ready to receive...")
    while True:
        connectionSocket, addr = serverSocket.accept()
        #Create a new thread and pass to connected_clients with the connectionSocket and addr as the parameters
        thread = threading.Thread(target=connected_clients, args=(connectionSocket, addr))
        #Start the thread
        thread.start()
def main():
    #Start the server
    start_server()

if (__name__ == "__main__"):
    main()
