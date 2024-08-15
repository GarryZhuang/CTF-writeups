## SillyGoose
There's no way you can guess my favorite number, you silly goose. Author: Connor Chang

#### Step-1:
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

#### Step-2:
Analyzing the code, we notice that the program generates a random number that is a google. We also see that we get to know if our guess is too high or too low.
We decide to use the Binary Search method to see if we can guess the random number in under 500 guesses.
Mathematical Proof:
`m = floor(2 / (low + high))`
$n \geq \log_{2}(10^{100}) = 100 \cdot \log_{2}(10) \approx 100 \cdot 3.321928 \approx 332.193$.

#### Step-3:
After executing the above script, we get a new image called `new_image.png` which is as follows:

<img src="new_image.png">

#### Step-4:
The image is then scanned using an online tool called [Aspose](https://products.aspose.app/barcode/recognize) which decodes the QR code and gives out the flag.

<img src="Flag.png">

#### Step-5:
Finally the flag becomes:
`CTFlearn{how_can_swapping_columns_hide_a_qr_code}`
