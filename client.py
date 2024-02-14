import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive welcome message from the server
response = client_socket.recv(1024).decode('utf-8')
print(response)

attempt = 0
max_attempts = 5

while attempt < max_attempts:
    # Input guess from the client
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Send guess to the server
    client_socket.send(str(guess).encode('utf-8'))

    # Receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    status_code, message = response.split(':', 1)
    print(message)

    if status_code == "200":
        break

    attempt += 1
    print("Attempts left:", max_attempts - attempt)

if attempt == max_attempts and status_code != "200":
    print("GAME OVER!")

# Close the connection
client_socket.close()
