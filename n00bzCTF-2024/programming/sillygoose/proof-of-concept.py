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