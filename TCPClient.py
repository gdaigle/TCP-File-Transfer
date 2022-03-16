from socket import *
import sys
#Constants
SIZE = 8192
FORMAT = "utf-8"
#if the command line argument does not equal 1
if(not sys.argv == 1):
    #print usage statement
    print("Usage: python3 TCPClient.py http://ip[:port]/path/to/file")
    sys.exit(1)

else:
    #initialize args as the command line argument
    args = sys.argv[1]

#This function parses through args and returns the ip
def find_ip():
    ip = ''
    slashCount = 0
    colonCount = 0
    for i in args:
        if(i == ':'):
            colonCount += 1
            if(colonCount == 2):
                break
        elif(i == "/"):
            slashCount += 1
            if(slashCount == 3):
                break
        ip += i
    return ip

#This function parses through args and returns the port number
def find_port():
    port = ''
    colonCount = 0
    slashCount = 0
    for i in args:
        if(i == ":"):
            colonCount += 1
        if(i == "/"):
            slashCount += 1
        if(colonCount == 2):
            if(slashCount < 3):
                port += i
            else:
                break
    #if the port is empty assign port to 80
    if(port == ''):
        port = ":80"
    return port

#This function parses through args and returns the file path
def find_path():
    path = ''
    colonCount = 0
    slashCount = 0
    for i in args:
        if(i == ":"):
            colonCount +=1
        if(i == "/"):
            slashCount += 1
        if(slashCount >= 3):
            path += i
    return path

def main():
    #Sets ip equal to the return value of find_ip()
    ip = find_ip()
    #Sets path equal to the return value of find_path()
    path = find_path()
    #Sets port equal to the return value of find_port()
    port = find_port()
    #Sets serverName equal to the ip address
    serverName = ip[7:]
    #Sets serverPort equal to the port number
    serverPort = int(port[1:])
    #Create the socket and connect to the server
    clientConnected = socket(AF_INET, SOCK_STREAM)
    clientConnected.connect((serverName,serverPort))
    #Create http GET request for file 
    send_request = f"GET {path} HTTP/1.1\r\n\r\n"
    #Send http GET request for file 
    clientConnected.send(send_request.encode(FORMAT))
    #Receive response and initialize to variable returned_response
    returned_response = clientConnected.recv(1024).decode()
    #Remove the escape characters from the variable
    returned_response = returned_response.split("\r")[0]
    #if response contains 200
    if("200" in returned_response):
        #print the response to the terminal
        print(returned_response)
        #Initializes returned_file to an empty byte-string
        returned_file = b''
        #Receives the file data
        file_received = clientConnected.recv(SIZE)
        while (file_received):
            #append returned_file to include file_received
            returned_file += file_received
            #Keeps receiving the file data until the while loop condition is broken
            file_received = clientConnected.recv(SIZE)
        #open file output
        with open("output", "wb") as output:
            #Writes the returned_file to output file
            output.write(returned_file)
        #Close socket connection
        clientConnected.close()
    #if response contains 404
    elif("404" in returned_response):
        #print the response to the terminal
        print(returned_response)
    #if response contains 505
    elif("505" in returned_response):
        #Splits the send request into ["GET", "<FILEPATH>", "HTTP/<Version>\r\n\r\n"]
        #and only keeps ["HTTP/<Version>\r\n\r\n"]
        http_version = send_request.split(" ")[2]
        #Splits the http_version into ["HTTP/<Version>", "\r\n\r\n"]
        #and only keeps ["HTTP/<Version>"]
        http_version = http_version.split("\r")[0]
        #print the response to the terminal
        print(http_version + returned_response)
    #if response does not contain 200, 404, or 505
    else:
        #print the response to the terminal
        print(returned_response)
        

if(__name__ == "__main__"):
    main()
