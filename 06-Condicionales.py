e1 = int(input("Edad 1: "))
e2 = int(input("Edad 2: "))
e3 = int(input("Edad 3: "))
if e1 != e2 and e1 != e3 and e2 != e3:
    if e1 > e2 and e1 > e3 : 
        print(f"Edad Mayor: {e1: .2f}")
    elif e1 < e2 and e1 < e3 :
        print(f"Edad menor: {e1: .2f}")
    if e2 > e1 and e2 > e3 : 
        print(f"Edad Mayor: {e2: .2f}")
    elif e2 < e1 and e2 < e3 :
        print(f"Edad Menor: {e2: .2f}")
    if e3 > e1 and e3 > e2 :
        print(f"Edad Mayor: {e3: .2f}")
    elif e3 < e1 and e3 < e2 :
        print(f"Edad Menor: {e3: .2f}")
else: 
    print("Tienen que ser edades diferentes")