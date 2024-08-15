import socket
import time

# Server connection parameters
HOST = 'IP_ADDR_REDACTED'
PORT = 41199

# Initialize the binary search parameters
low = 0
high = pow(10, 100)
guess_count = 0

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Log the start time
    start_time = int(time.time())
    
    while True:
        # Check if time limit exceeded
        if int(time.time()) > start_time + 60:
            print("You ran out of time, you silly goose")
            break
        
        # Calculate the middle point
        mid = (low + high) // 2
        guess_count += 1
        
        # Send guess to the server
        s.sendall(f"{mid}\n".encode())
        
        # Receive and decode the response
        response = s.recv(4096).decode().strip()
        
        if "congratulations" in response:
            print(f"Congrats! The number is {mid}. Found in {guess_count} guesses.")
            print("Server response:", response)
            break
        elif "too small" in response:
            print(f"[Guess {guess_count}] {mid} is too low.")
            low = mid + 1
        elif "too large" in response:
            print(f"[Guess {guess_count}] {mid} is too high.")
            high = mid - 1
        else:
            print(f"Unexpected server response: {response}")