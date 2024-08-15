## StegOnline🌐
This is an introductory steganography challenge. Here is some guidance to help you on your way.

1. You will need an online image steganography tool. Which tool? The name of the tool is provided somewhere.
2. One of the bits has been corrupted in the R, G, and B bit representations.
3. Extract the corrupted bits stored in the R, G, and B bit representations.


#### ➡Step-1:
The tool is ***Steg Online*** based on the file name.

#### ➡Step-2:
Analysis of the color plane indicates there is an issue with R0, G0, B0. Maybe there is hidden data?

<center><img src="colorplane.jpg"></center>

#### ➡Step-3:
Created the proof of concept on my client-side to prevent the server from receving unnecessary traffic 

```py
# ============================================
# Proof Of Concept
# By Garry Zhuang 2024
# ============================================
# This shows that the CTF task (SillyGoose) can be completed in less than 400 tries
#
# This uses the binary search method,
# calculated to take a maximum 333 tries/attempts.
#
# To run:
# ./program.py

from random import randint
import time

ans = randint(0, pow(10, 100))  # Generate the random number
start_time = int(time.time())  # Log the start time

while True:

    # We have 60 seconds to complete this task.
    if int(time.time()) > start_time + 60: 
       print("you ran out of time you silly goose") 
       break

    low = 0
    high = pow(10, 100)
    guess_count = 0
    
    while low <= high:
        # Calculate the middle point
        mid = (low + high) // 2
        guess_count += 1
        
        if mid < ans:
            print(f"[Guess {guess_count}] {mid} is too low.")
            
            low = mid + 1
        elif mid > ans:
            print(f"[Guess {guess_count}] {mid} is too high.")
            high = mid - 1
        else:
            print(f"Congrats! The number is {mid}. Found in {guess_count} guesses.")
            break
    break
```

#### ➡Step-4:
Peform the code on the server and see if it works!

```py
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
```


#### 👑Step-4:
The server outputs the flag:
`n00bz{y0u_4r3_4_sm4rt_51l1y_g0053}`
