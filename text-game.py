

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player:
    def __init__(self):
        self.__inventory = []

    def check_inventory(self):
        print(self.__inventory)
    
    def add_to_inventory(self, item):
        self.__inventory.append(item)

    def is_item(self, check):
        if check in self.__inventory:
            return True
        else:
            return False

class Objects:
    def __init__(self, place, item):
        self.__place = place
        self.__item = item
        self.__place_inventory = []
        self.__place_inventory.append(item)


    def take_item(self):
        player.add_to_inventory(self.__item)
        self.__place_inventory.remove(self.__item)
        pass

    def place_item(self):
        Player.__inventory.remove(self.__item)
        pass


def numsfunc():
    import nums


player = Player()
alley = Objects("Alley", "fish")
pantry = Objects("pantry", "sushi")

def route1():
    # create items for alleyway
    print("\nYou quickly navigate through the alleyway's sharp corners and arrive at a dead end.")
    print("You see a dumpster next to a suspicious door. This is the origin of the fishy smell.")
    print("You could probably manage to get in and out of the dumpster without getting stuck. Will you peek in?")
    while True:
        ac1 = input(bcolors.HEADER + "Type 'peek' or 'turn back'\n" + bcolors.ENDC)
        if ac1 == "peek":
            print("\nYou see a bunch of fish inside. Take one?")
            while True:
                ac2 = input("Type y/n\n")
                if ac2 == "y":
                    alley.take_item()
                    player.check_inventory()
                    print("\nYou take the fish and go back to the beginning")
                    quest1()
                    break
                elif ac2 == "n":
                    print("\nYou turn around and go back to the beginning")
                    quest1()
                    break

            break
        elif ac1 == "turn back":
            quest1()
            break
        else: 
            print(bcolors.FAIL + "Please choose one of the routes." + bcolors.ENDC)


def route2():
    print("\nSqueezing through the fence, you're now at the far corner of a backyard with an overgrown lawn.")
    print("You can barely see anything behind the grass, but you hear a suspicious sound up ahead.")
    print("Will you go straight ahead or along the fence to the right?")

    while True:
        bc1 = input(bcolors.HEADER + "Type 'right' or 'straight'\n" + bcolors.ENDC)
        if bc1 == "right":
            print("\nYou're now next to a house. Through an open window you hear people talking.")
            print("Will you jump inside, or turn around?")
            while True:
                bc2 = input(bcolors.HEADER + "Type 'jump' or 'turn around'\n" + bcolors.ENDC)
                if bc2 == "jump":
                    print("\nYou smell leftover sushi behind a locked door.")
                    print("Can you guess the correct combination?")

                    numsfunc()
                    pantry.take_item()
                    player.check_inventory()

                    break

                elif bc2 == "turn around":
                    route2()
                    break
                else:
                    print(bcolors.FAIL + "Please choose one of the options." + bcolors.ENDC)
            break

        elif bc1 == "straight":
            print("\nYou see a scared kitten. Maybe if you offer it food, it will tell you where to go?")
            while True:
                bc3 = input(bcolors.HEADER + "Type 'offer food'\n" + bcolors.ENDC)
                if bc3 == "offer food":
                    if player.is_item("fish"):
                        print("\nyou offer the fish from earlier")
                        
                        break
                    else:
                        print(bcolors.WARNING + "\nyou have no food to offer and go back to the beginning." + bcolors.ENDC)
                        route2()
                        break
                else:
                     print(bcolors.FAIL + "Try again" + bcolors.ENDC)

            break
        else: 
            print(bcolors.FAIL + "Please choose one of the routes." + bcolors.ENDC)


def quest1():
    print("\nRoute 1: a dark and narrow alleyway that smells a little fishy...")
    print("Route 2: through a hole in a fence.")

    while True:
        choice1 = input(bcolors.HEADER + 'Type "route1" or "route2"\n' + bcolors.ENDC)
        if choice1 == "route1":
            route1()
            break
        elif choice1 == "route2":
            route2()
            break
        else:
            print(bcolors.FAIL + "Please choose one of the routes." + bcolors.ENDC)



def main():
    print(bcolors.HEADER + "welcome, traveler! Would you like to embark on a journey?" + bcolors.ENDC)
    while True:
        embark = input("y/n\n")
        if embark == "y":
            print("\nYour first quest begins with a choice between two routes.")
            quest1()
            break
        elif embark == "n":
            print(bcolors.BOLD + "Until next time..." + bcolors.ENDC)
            break
        else:
            print(bcolors.FAIL + "WHAT YA SAY??" + bcolors.ENDC)
        

main()