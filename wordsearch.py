# Create a function which takes in a word and then searches for the word within the text

# Open up the file called "Monologue.txt"
monologueFile = open('monologue.txt', 'r')

# Read the text contained within the file
monologueText = monologueFile.read()

# Add a space before the word so as to make sure that it is independent
monologueSplit = monologueText.split(' ')

# Search for any instances of the word provided
print(monologueSplit[0])
print(monologueSplit[1])
print(monologueSplit[2])
print("------")

# If the word is found, count up how many times it appears by splitting the text on the word and counting the length of the list returned

wordSearched = input("Type in a word to search for in this file: ")

# Print out how many times the word was found

if wordSearched.find(wordSearched) > -1:
    print(wordSearched)
    print("horray")
else:
    print("womp")

    # If no instances of the word was found, print out that the word is not in the text

    # Collect a word from the user

    # Pass the word to search into the function created
