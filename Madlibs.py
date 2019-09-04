noun = input("Enter noun here: ")
pronoun = input("Enter pronoun here: ")
verb = input("Enter verb here: ")
adjective = input("Enter adjective here: ")
plural_noun = input("Enter plural noun here: ")
POF = [noun, pronoun, verb, adjective, plural_noun]


def madlib():
    print("\033[1;34;40m") #changes text blue
    print("It was Thanksgivig, and the scent of succulent roast " + POF[0])
    print("wafted through my house " + POF[1])
    print("said it's time to go " + POF[2])
    print("my mother called. I couldnt wait to get part of the body " + POF[4])
    print("on that " +  POF[3] + " Thanksgivig meal ")
    print("My family sat around the dining-room " + POF[0])
    print("The table was laid out with every kind of " + POF[0] + " imaginable ")
    print("There was a basket of hot buttered " + POF[4] + " and glasses of"
    + " sparkling wine ")
    print("The " + POF[3] + " turkey sat, steaming.")


madlib()

# Madlib take from:
# https://hobbylark.com/party-games/How-to-Make-Your-Own-Mad-Libs
