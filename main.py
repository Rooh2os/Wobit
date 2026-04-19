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

wordlewords = data.split()

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
