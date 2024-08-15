## StegOnline🌐
This is an introductory steganography challenge. Here is some guidance to help you on your way.

1. You will need an online image steganography tool. Which tool? The name of the tool is provided somewhere.
2. One of the bits has been corrupted in the R, G, and B bit representations.
3. Extract the corrupted bits stored in the R, G, and B bit representations.


#### ➡Step-1:
We are given `sillygoose.py` which is as follows:

```py
from random import randint
import time
ans = randint(0, pow(10, 100))
start_time = int(time.time())
turns = 0
while True:
    turns += 1

    inp = input()

    if int(time.time()) > start_time + 60:
       print("you ran out of time you silly goose") 
       break

    if "q" in inp:
        print("you are no fun you silly goose")
        break

    if not inp.isdigit():
        print("give me a number you silly goose")
        continue

    inp = int(inp)
    if inp > ans:
        print("your answer is too large you silly goose")
    elif inp < ans:
        print("your answer is too small you silly goose")
    else:
        print("congratulations you silly goose")
        f = open("/flag.txt", "r")
        print(f.read())

    if turns > 500:
        print("you have a skill issue you silly goose")
```

#### ➡Step-2:
Analyzing the code, we notice that the program generates a random number that is a google. We also see that we get to know if our guess is too high or too low.
We decide to use the Binary Search method to see if we can guess the random number in under 500 guesses.
**Mathematical Proof:**
$n \geq \log_{2}(10^{100}) = 100 \cdot \log_{2}(10) \approx 100 \cdot 3.321928 \approx 332.193$.

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
