l1 = "1│2│3"
l2 = "4│5│6"
l3 = "7│8│9"
divisor = "─┼─┼─"
game = False
opt = ["1","2","3","4","5","6","7","8","9"]

def valid_input():
    x = input()
    if x in opt:
        print("good")
        opt.remove(x)
        return int(x)
    else:
        print("invalid")
        return valid_input()

print(l1)
print(divisor)
print(l2)
print(divisor)
print(l3)

while game == False:
    print("Player 1 input:")
    inp = valid_input()
    if inp == 1:
        l1 = "x"+l1[1:5]
    elif inp == 2:
        l1 = l1[:2]+"x"+l1[3:5]
    elif inp == 3:
        l1 = l1[:4]+"x"
    if inp == 4:
        l2 = "x"+l2[1:5]
    elif inp == 5:
        l2 = l2[:2]+"x"+l2[3:5]
    elif inp == 6:
        l2 = l2[:4]+"x"
    if inp == 7:
        l3 = "x"+l3[1:5]
    elif inp == 8:
        l3 = l3[:2]+"x"+l3[3:5]
    elif inp == 9:
        l3 = l3[:4]+"x"
    print(l1)
    print(divisor)
    print(l2)
    print(divisor)
    print(l3)
    if l1[0]+l1[2]+l1[4] == "xxx":
        print("Player 1 won")
        game = True
    if l2[0]+l2[2]+l2[4] == "xxx":
        print("Player 1 won")
        game = True
    if l3[0]+l3[2]+l3[4] == "xxx":
        print("Player 1 won")
        game = True
    if l1[0]+l2[2]+l3[4] == "xxx":
        print("Player 1 won")
        game = True
    if l3[0]+l2[2]+l1[4] == "xxx":
        print("Player 1 won")
        game = True
    if l1[0]+l2[0]+l3[0] == "xxx":
        print("Player 1 won")
        game = True
    if l1[2]+l2[2]+l3[2] == "xxx":
        print("Player 1 won")
        game = True
    if l1[4]+l2[4]+l3[4] == "xxx":
        print("Player 1 won")
        game = True
    if len(opt) == 0:
        game = True
        print("Stalemate")

    if game == True:
        break

    print("Player 2 input:")
    inp = valid_input()
    if inp == 1:
        l1 = "o"+l1[1:5]
    elif inp == 2:
        l1 = l1[:2]+"o"+l1[3:5]
    elif inp == 3:
        l1 = l1[:4]+"o"
    if inp == 4:
        l2 = "o"+l2[1:5]
    elif inp == 5:
        l2 = l2[:2]+"o"+l2[3:5]
    elif inp == 6:
        l2 = l2[:4]+"o"
    if inp == 7:
        l3 = "o"+l3[1:5]
    elif inp == 8:
        l3 = l3[:2]+"o"+l3[3:5]
    elif inp == 9:
        l3 = l3[:4]+"o"
    print(l1)
    print(divisor)
    print(l2)
    print(divisor)
    print(l3)
    if l1[0]+l1[2]+l1[4] == "ooo":
        print("Player 2 won")
        game = True
    if l2[0]+l2[2]+l2[4] == "ooo":
        print("Player 2 won")
        game = True
    if l3[0]+l3[2]+l3[4] == "ooo":
        print("Player 2 won")
        game = True
    if l1[0]+l2[2]+l3[4] == "ooo":
        print("Player 2 won")
        game = True
    if l3[0]+l2[2]+l1[4] == "ooo":
        print("Player 2 won")
        game = True
    if l1[0]+l2[0]+l3[0] == "ooo":
        print("Player 2 won")
        game = True
    if l1[2]+l2[2]+l3[2] == "ooo":
        print("Player 2 won")
        game = True
    if l1[4]+l2[4]+l3[4] == "ooo":
        print("Player 2 won")
        game = True