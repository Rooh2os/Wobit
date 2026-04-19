import toml

#Make wordle words list
try:
    with open("wordle-words.txt","r") as file:
        data = file.read()

except(FileNotFoundError):
    import requests
    data = requests.get("https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt")
    with open("wordle-words.txt","w") as file:
        file.write(data.text)
        data = file.read()

wordlist = data.split()

#Make/get config
try:
    with open("config.toml","r") as file:
        config = toml.load(file)

except(FileNotFoundError):
    print("Config not found.\nGenerating new config...")

    config = {
                "general": {
                    "show only top word": True
                },
                "debug": {
                    "print debug logs": False
                }
            }
    with open("config.toml","w") as file:
        toml.dump(config,file)
    
    print("New config generated.\nPlease look at the config, then restart the program to apply the settings.")

#Intro
print("Welcome to Wobit (don't ask where the name comes from)\nA Wordle bot developed by Rooh2os\n")

#Main loop

for guess in range(6):
    #DEBUG; prints the wordlist after every word
    if config["debug"]["print debug logs"]:
        print(wordlist)
    
    #Use the config to determine whether to give the user the choice of the word or choose it automagicly
    if config["general"]["show only top word"]:
        print(f"Current top word: {wordlist[0]}")
        inputword = wordlist[0]
    else:
        print(f"Current wordlist:\n{wordlist}")
        #Sterilize user input
        inputword = None
        while inputword == None:
            try:
                inputword = input("What word did you use?\n")
                if inputword not in wordlist:
                    raise(ValueError)
            except(ValueError,TypeError):
                print("Oops! Thats not a valid choice!\nPlease choose a valid option.")
                inputword = None
    
    for letter in inputword:
        #Sterilize user input (Code most likely flawed)
        #Why cant humans just be perfect and put in the right numbers?
        gyg = None
        while gyg == None:
            try:
                print(f"The current letter is '{letter}'.")
                gyg = int(input("1: Grey; Letter is not in word\n2: Yellow; Letter is in word, but it's not in the right spot\n3: Green; Letter is in word, and it's in the right spot\nChoose an option\n"))

                #Looks like this:
                #The current letter is 'a'.
                #1: Grey; Letter is not in word
                #2: Yellow; Letter is in word, but it's not in the right spot
                #3: Green; Letter is in word, and it's in the right spot
                #Choose an option

                if gyg > 3 or gyg < 1:
                    raise(TypeError)
            except(TypeError,ValueError):
                print("Oops! Thats not a valid choice!\nPlease choose a valid option.")
                gyg = None
        
        #Var name 'gyg' means 'green yellow gray' representing the 3 options the user can choose from

        #Logic for bot; does word removal based on gyg input
        #temp placeholder code until i get off my bum and actually write it
        if gyg == 1:
            pass
        elif gyg ==2:
            pass
        else:
            pass