import random
import string
from random import shuffle


def password_maker():
    x = input("Wanna password magic lad?").upper()
    w = []
    def here_we_go_lads():
        if x == "YES":
            y = input("Do you want strong, mid or weak password?").upper()
            if y == "STRONG":
                for i in random.sample(range(1,11), random.randint(7,10)):
                    w.append(random.choice(list(string.ascii_letters)))
                for i in random.sample(range(1, 11), random.randint(7, 10)):
                    w.append(str(i))
                for i in random.sample(range(1, 11), random.randint(7, 10)):
                    w.append(random.choice(list(string.punctuation)))
            elif y == "MID":
                for i in random.sample(range(1,11), random.randint(4,6)):
                        w.append(random.choice(list(string.ascii_letters)))
                for i in random.sample(range(1, 11), random.randint(4, 6)):
                        w.append(str(i))
                for i in random.sample(range(1, 11), random.randint(4, 6)):
                        w.append(random.choice(list(string.punctuation)))
            elif y == "WEAK":
                for i in random.sample(range(1, 11), random.randint(1, 3)):
                        w.append(random.choice(list(string.ascii_letters)))
                for i in random.sample(range(1, 11), random.randint(1, 3)):
                        w.append(str(i))
                for i in random.sample(range(1, 11), random.randint(1, 3)):
                        w.append(random.choice(list(string.punctuation)))
            elif y == "EXIT":
                print("See you next time!")
            else:
                print("Choose strong, mid, weak or exit if you are no longer intrested")
                here_we_go_lads()
            shuffle(w)
            your_password = "".join(w)
            print("Here is your password: ", your_password)
        elif x == "NO":
            print("Then why are we here? Just to suffer?")
        elif x == "MAYBE":
            print("You gonna be the one to save me")
            password_maker()
        else:
            print("Please, choose yes or no")
            password_maker()

    here_we_go_lads()

password_maker()
