# Coder Matthew Gutierrez# Coder: Matthew Gutierrez
# # CIT 95 String and Lists Program

#Intro

print("Welcome to Mac Mac's Python Strings and Lists Program.\n\n" + '"Python is an amazing programming language. It is versatile, easy to learn, and powerful."\n')

#restart

def script():

    #beginning variables

    text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
    upper_case = text.upper()
    lower_case = text.lower()
    text_length = len(text)

    #user input

    print ("Let's begin.\n\nThe above phrase has an index length of "+ str(text_length) + "\n")
    start = int(input("To begin the program enter an index number to create a substring: "))
    print("Your substring starts at index " + str(start))
    end = int(input("Enter an index number to end with: "))
    print("Your substring ends at index " + str(end)+ "\n")
    replacing = input("Now retype a word you would like to replace: ")
    print("The word selected is " + '"' + replacing + '"')
    replacement = input("Ok and what will be the replacing word? ")
    print ('"I like it as you like it." Your word replacement is ' + '"' + replacement + '".\n')
    user_char = input("Now please choose a single letter or a single character or a string of letters or characters "
                      "from the phrase: ")
    print ('You chose "' + user_char + '" as your selection.\n')

    print ("Thanks. Now I will analyze text...\n")

    # functions
    def user_substring(text):
        substring = text[start:end].replace(replacing, replacement)
        print('This is your substring: "' + substring + '"\n')
    def word_split(text):
        word_splitter = text.replace('.,', '').split(' ')
        splitter_count = len(word_splitter)
        print("Excluding punctuation there are " + str(splitter_count) + " words.\n")
    def split_sentences(text):
        sentence_splitter = text.split('.')
        print(sentence_splitter)
    def char_counter(text, user_char):
        counter = 0
        text_array = text
        for i in range (len(text_array)):
            if (user_char == text_array[i]):
                counter += 1
        print("Your chosen character occured " + str(counter) + " times.\n")
    def reverse (text):
        text_split = text.split(" ")
        reverse_text = ''
        for i in range(len(text_split)-1, -1, -1):
            reverse_text += text_split[i] + ' '
        print(reverse_text + "\nHa Ha! That's a good trick right?\n")

    def out_print():
        print("I have converted the string to Uppercase letters: " + upper_case + "\n")
        print("I have converted the string to Lowercase letters: " + lower_case + "\n")
        word_split(text)
        user_substring(text)
        split_sentences(text)
        char_counter(text, user_char)
        reverse(text)

    #executing

    print("Text analyzed.\n")
    out_print()

    #restar from user input

    restart = input("That was fun! let's go again. Would you like to change your inputs? ").upper()
    if restart == "YES" or restart == "Y":
        print('I understand you said "' + restart + '"\n')
        correct_restart = input("correct? y/n: ").lower()
        print('I understand you said "' + correct_restart + '"\n')
        if correct_restart == "y":
            print("Ok let's go again!\n\n")
            script()
        else:
            print("Thank you for testing Mac Mac's string's and lists program. Goodbye.")
    else:
        print('I understand you said "' + restart + '"\n')
        no_restart = input("Close program? y/n: ").lower()
        print('I understand you said "' + no_restart + '"\n')
        if no_restart == "y":
            print("Thank you for testing Mac Mac's string's and lists program. Goodbye.")
        if no_restart == "n":
            print("Ok let's go again!\n\n")
            script()
        else:
            print("Thank you for testing Mac Mac's string's and lists program. Goodbye.")
script()