min = 1
max = 100

print(f"""Gondolj egy számra {min} és {max} között!""")

answer = "x"
prevguess = -1
guess = -2

while answer!= "e":
    prevguess = guess
    guess = (min + max) // 2
    
    if guess == prevguess: 
        print("Ne szórakozz velem!")
        answer = "e" or "E"
    else:
        print(f"""Erre a számra gondoltam: {guess}""")

        answer = input("Kisebb (k), nagyobb(n) vagy egyenlő(e)?")

        if answer == "k" or answer == "K":
            max = guess
        elif answer == "n" or answer == "N":
            min = guess
        elif answer == "e" or answer == "E":
            print(f"""{guess}-ra gondoltál""")
        else: 
            print("Ez nem jó válasz!")

# HF: Hanyadikra találta el? 