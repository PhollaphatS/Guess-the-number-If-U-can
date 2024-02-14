import socket
import random

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print("Secret number:", secret_number)

while True:
    # Wait for a connection
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)
    
    # Send a message to the client
    client_socket.send("200: Welcome to the Guessing Game!".encode('utf-8'))

    attempt = 0
    
    while attempt < 5:
        # Receive guess from client
        guess = client_socket.recv(1024).decode('utf-8')
        
        # Check guess
        try:
            guess = int(guess)
            if guess < secret_number:
                client_socket.send("404: Too low!".encode('utf-8'))
            elif guess > secret_number:
                client_socket.send("404: Too high!".encode('utf-8'))
            else:
                client_socket.send("200: Congratulations! You guessed the number!".encode('utf-8'))
                break
        except ValueError:
            client_socket.send("404: Please enter a valid integer.".encode('utf-8'))
        
        attempt += 1
    
    if attempt == 5:
        client_socket.send("404: Sorry, you've run out of attempts!".encode('utf-8'))
    
    # Close the connection
    client_socket.close()
    
    # Close the server socket after client guesses the number
    server_socket.close()
    break
