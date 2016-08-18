from os import listdir
import json

# This script cleans / formats the jokes and concatonates them all into
# one main json file.


# Formats the jokes a bit
def cleanJokes(jokes):
    for joke in jokes:
        # Remove needless new lines.
        joke["part2"] = joke["part2"].replace("\n", " ").strip()

        # Remove everything after 'edit:', because it's not part of the joke.
        try:
            index = joke["part2"].lower().index("edit:")
            joke["part2"] = joke["part2"][:index]
        except:
            pass

    return jokes

jokes = []

# Iterate over all segment files, merge all arrays into one
for file in listdir("./data", ):
    curFile = open("./data/" + file, "r")
    data = json.load(curFile)
    jokes.extend(cleanJokes(data))

# format final array in json and save to file
output = open("all.json", "w")
output.write(json.dumps(jokes, indent=2))
output.close()
