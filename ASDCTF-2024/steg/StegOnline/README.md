## StegOnline🌐
This is an introductory steganography challenge. Here is some guidance to help you on your way.

1. You will need an online image steganography tool. Which tool? The name of the tool is provided somewhere.
2. One of the bits has been corrupted in the R, G, and B bit representations.
3. Extract the corrupted bits stored in the R, G, and B bit representations.


#### ➡Step-1:
The tool is ***Steg Online*** based on the file name.

#### ➡Step-2:
Analysis of the color plane indicates there is an issue with R0, G0, B0. Maybe there is hidden data?

<center><img src="colorplane.png"></center>

#### ➡Step-3:
Using StegOnline tool (https://georgeom.net/StegOnline/extract) to extract the data results in:

ASCII Output:
```
Name: Al  ex M.Age  : 32.Cit  y: Canbe  rra.Favo  urite Di  nosaur:   Spinosau  rus..Nam  e: Georg  e A.Age:   7.City:   Sydney.  Favourit  e Dinosa  ur: Velo  ciraptor  ..Name:   Mary D.A  ge: 56.C  ity: Mel  bourne.F  avourite   Dinosau  r: Bront  osaurus.  .Name: S  ophia C.  Age: 22.  City: Pe  rth.Favo  urite Di  nosaur:   Tyrannos  aurus Re  x..Name:   Alex M.  Age: 32.  City: Ca  nberra.F  avourite   Dinosau  r: Spino  saurus..  Name: Ge  orge A.A  ge: 7.Ci  ty: Sydn  ey.Favou  rite Din  osaur: V  elocirap  tor..Nam  e: Mary   D.Age: 5  6.City:   Melbourn  e.Favour  ite Dino  saur: Br  ontosaur  us..Name  : Sophia   C.Age:   22.City:   Perth.F  avourite   Dinosau  r: Tyran  nosaurus   Rex..Na  me: Alex   M.Age:   32.City:   Canberr  a.Favour  ite Dino  saur: Sp  inosauru  s..Name:   George   A.Age: 7  .City: S  ydney.Fa  vourite   Dinosaur  : Veloci  raptor..  Name: Ma  ry D.Age  : 56.Cit  y: Melbo  urne.Fav  ourite D  inosaur:   Brontos  aurus..N  ame: Sop  hia C.Ag  e: 22.Ci  ty: Pert  h.Favour  ite Dino  saur: Ty  rannosau  rus Rex.  .Name: A  lex M.Ag  e: 32.Ci  ty: Canb  erra.Fav  ourite D  inosaur:   Spinosa  urus..Na  me: Geor  ge A.Age  : 7.City  : Sydney  .Favouri  te Dinos  aur: Vel  ocirapto  r..Name:   Mary D.  Age: 56.  City: Me  lbourne.  Favourit  e Dinosa  ur: Bron  tosaurus  ..Name:   Sophia C  .Age: 22  .City: P  erth.Fav  ourite D  inosaur:   Tyranno  saurus R  ex..Name  : Stego   Saurus.A  ge: 100.  City: Ju  rassic P  ark.Favo  urite Di  nosaur:   ASDCTF{N  OM_NOM}.  .Name: A  lex M.Ag  e: 32.Ci  ty: Canb  erra.Fav  ourite D  inosaur:   Spinosa  urus..Na  me: Geor  ge A.Age  : 7.City  : Sydney  .Favouri  te Dinos  aur: Vel  ocirapto  r..Name:   Mary D.  Age: 56.  City: Me  lbourne.  Favourit  e Dinosa  ur: Bron  tosaurus  ..Name:   Sophia C  .Age: 22  .City: P  erth.Fav  ourite D  inosaur:   Tyranno  saurus R  ex.....P  ...D4(..  M ......  .bE=.j..  h.N.E.<.  ...a@O9.  B...u ".  ..Y.....  D..DF..0  ....=...  .xq.....  I$.I$...  cuR.I%jA  $.J.RI.E  B<...P..  ..Z}..[.  ......+.  ..K..i.T  .H..C..0  `.l.X.`.  ..s`..z)  Hd....Zw  ..A&.H..  ....m=.o  ..NR.`&.  .....H..  ......Zo  &H$#. "o  `..)..T.  S.......  7. ....J  .,...$.R  a.....B#  ,...Z..A  ..Z.>.$.  ...A.:.%  .I..)!`.  ..,P"...  ..Q.Z...  .\......  1..!....  I$.I$./.  ..,...B.  !jU[RI..  ....H."!  .)......  :.....(G  c"..m.K@  .C......  ......`$  .$......  )....(..  L.I*.H..  y)..I.H-  ..n.....  .N..*A.2  ...A..$.  .....`..  B.G.....  ........  ....>...  I@. .;.T  ..[#..!z  
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
