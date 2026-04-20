import toml

def printlist(list:list,prefix:str=""):
    print(prefix)
    for item in list:
        print(f"{list.index(item)+1}. {item}")

def process_grey(wordlist:list,inputword:str):
    ptr = 0

    #Check if the letter is in the word
    #   ├─ yes; remove the word then advance to the next word (ptr does not need to be increased as by removing a word the whole list gets shifted down making ptr relatively increased by 1)
    #   └─ no; move on to next word
    while ptr < len(wordlist):
        if inputword[letter] in wordlist[ptr]:
            wordlist.remove(wordlist[ptr])
        else:
            ptr += 1
    return(wordlist)

def process_yellow(wordlist:list,inputword:str,letter:int):
    ptr = 0
    while ptr < len(wordlist):
        word = wordlist[ptr] #had to do this because py is picky. why cant i just do `wordlist[ptr].index` ?
        
        #Check if letter is in word
        #   ├─ yes; check if letter is in the same spot as the yellow letter
        #   │   ├─ yes; remove word
        #   │   └─ no; keep word and increment ptr (pointer)
        #   └─ no; remove word
        if (not inputword[letter] in word) or word[letter] == inputword[letter]:
            wordlist.remove(word)
        else:
            ptr += 1
    
    return(wordlist)

def process_green(wordlist:list,inputword:str):
    ptr = 0
    while ptr < len(wordlist):
        word = wordlist[ptr]

        #Check if letter in word
        #   ├─ yes; check if letter is in the same spot as it is in word
        #   │   ├─ yes; increment ptr
        #   │   └─ no; remove word
        #   └─ no; remove word
        try:
            if word.index(inputword[letter]) == letter:
                ptr += 1
            else:
                raise(ValueError)
        except ValueError:
            wordlist.remove(word)
    return(wordlist)

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
                },
            }
    with open("config.toml","w") as file:
        toml.dump(config,file)
    
    print("New config generated.\nPlease look at the config, then restart the program to apply the settings.")

#Intro
print("Welcome to Wobit (don't ask where the name comes from)\nA Wordle bot developed by Rooh2os\n")

#Main loop

guess = 1
while len(wordlist) > 1 and guess < 6:

    print(f"\nCurrent top word: {wordlist[0]}\nRemaining words: {len(wordlist)}")
    inputword = wordlist[0]
    
    letter = 0
    while letter < len(inputword):
        #Sterilize user input (Code most likely flawed)
        #Why cant humans just be perfect and put in the right numbers?
        gyg = None
        while gyg == None:  
            try:
                print(f"\nThe current letter is '{inputword[letter]}' in spot {letter + 1}.")
                print("1: Grey; Letter is not in word\n2: Yellow; Letter is in word, but it's not in the right spot\n3: Green; Letter is in word, and it's in the right spot")

                print("Choose an option")

                gyg = int(input())
                


                #Looks like this:
                #
                #The current letter is 'x' in spot y.
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
            wordlist = process_grey(wordlist,inputword)

        elif gyg ==2: #Yellow letter semi-removal

            process_yellow(wordlist,inputword,letter)
                
        elif gyg == 3: #Green letters
            
        letter += 1
    guess += 1

if len(wordlist) == 1:
    print("Congrats on beating Wordle!")
else:
    print("Sorry I let you down ☹")

printlist(wordlist,"Final valid words:")