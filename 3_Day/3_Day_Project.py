print('''
                               __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\
                            ;  bug
''')

print("Welcome to Treasure island. Ypur mission is to find the treasure!\n Lets start the Game\n")


firstDescision = input("You wana go left or right").lower()

if firstDescision == "left":
    print("Wise Desision child")
    secondDescision = input("Water here do wanna swim or wait for boat?").lower()
    if secondDescision == "wait":
        print("Nice")
        thiredDescison = input("Choose a door red, yellow or blue?").lower()
        if thiredDescison == "yellow":
            print("You Wins")
        elif thiredDescison == "red":
            print("Ouch! Burned by fire Game Over!")
        elif thiredDescison == "blue":
            print("You became food for beasts.")
        else:
            print("Game Over!!!")
    else:
        print("Opps deep water!")
else:
    print("You died wrong way")

