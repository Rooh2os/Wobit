import toml

#Make wordle words list
try:
    with open("wordle-words.txt","r") as file:
        data = file.read()

except FileNotFoundError:
    import requests
    data = requests.get("https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt")
    with open("wordle-words.txt","w") as file:
        file.write(data.text)
        data = data.text

wordlist = data.split()

#Make/get config
try:
    with open("config.toml","r") as file:
        config = toml.load(file)

except FileNotFoundError:
    print("Config not found.\nGenerating new config...")

    config = {
                "general": {
                    "show only top word": True,
                    "use custom starting word": False, #this will eventually be implemented when main logic is done
                    "custom starting word": "crane"
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
        #This print will be replaced by a printlist function
        print(f"Current wordlist:\n{wordlist}")
        #Sterilize user input
        inputword = None
        while inputword == None:
            try:
                inputword = input("What word did you use?\n")
                if inputword not in wordlist:
                    raise(ValueError)
            except (ValueError,TypeError):
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
            except (TypeError,ValueError):
                print("Oops! Thats not a valid choice!\nPlease choose a valid option.")
                gyg = None
        
        #Var name 'gyg' means 'green yellow gray' representing the 3 options the user can choose from

        #Logic for bot; does word removal based on gyg input

        if gyg == 1: #Grey letter removal
            ptr = 0
            
            if config["debug"]["print debug logs"]:
                print(len(wordlist)) #debug please tell me what I did this time
            

            #Check if the letter is in the word
            #   ├─ yes; remove the word then advance to the next word (ptr does not need to be increased as by removing a word the whole list gets shifted down making ptr relatively increased by 1)
            #   └─ no; move on to next word
            while ptr < len(wordlist):
                if letter in wordlist[ptr]:
                    wordlist.remove(wordlist[ptr])
                else:
                    ptr += 1
    
                if config["debug"]["print debug logs"]: #debug oh, debug. please solve my problems mr. debug
                    print(f"ptr: {ptr}")
                    print(f"wordlist len: {len(wordlist)}")

        elif gyg ==2: #Yellow letter semi-removal

            ptr = 0
            while ptr < len(wordlist):
                word = wordlist[ptr] #had to do this because py is picky. why cant i just do `wordlist[ptr].index` ?
                
                if config["debug"]["print debug logs"]:
                    print(f"not letter in word or word.index: {not letter in word}")
                    try:
                        print(f"word.index(letter) == inputword.index(letter): {word.index(letter) == inputword.index(letter)}")
                    except ValueError:
                        pass #ok to pass here, just debug code
                
                #Check if letter is in word
                #   ├─ yes; check if letter is in the same spot as the yellow letter
                #   │   ├─ yes; remove word
                #   │   └─ no; keep word and increment ptr (pointer)
                #   └─ no; remove word
                if not letter in word:
                    wordlist.remove(word)
                elif word.index(letter) == inputword.index(letter):
                    wordlist.remove(word)
                else:
                    ptr += 1
                
                if config["debug"]["print debug logs"]:
                    #print(f"wordlist: {wordlist}") #need to debug the debug
                    print(f"ptr: {ptr}")
                    print(f"wordlist len: {len(wordlist)}")
                    
        else:
            pass #temp
        
        if config["debug"]["print debug logs"]: #I should stop debugging and just write better code
            print(f"wordlist: {wordlist}")

            print(f"inputword in wordlist: {inputword in wordlist}")