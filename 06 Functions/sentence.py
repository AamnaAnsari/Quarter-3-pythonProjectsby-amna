# Helper function to create a sentence based on part of speech
def make_sentence(word, part_of_speech):
    # Check the part of speech
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")

# program ko run krne ke lie main function
def main():
    # Ask the user for a word
    word = input("Please type a noun, verb, or adjective: ")

    # Ask the user for the part of speech type
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the function with the word and part of speech
    make_sentence(word, part_of_speech)

# Run the main function
main()
