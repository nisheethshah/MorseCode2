# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 01/04/2018
# Last Modified Date: 03/04/2018
# Assignment 2: Task 5: Putting all the classes together
# -----------------------------------------------------------------------------

# Importing library & classes from another files
from decoder_29599644 import Decoder
from character_29599644 import CharacterAnalyser
from word_29599644 import WordAnalyser
from sentence_29599644 import SentenceAnalyser
import re


def input_function(message_for_input):
    """"Method to take input from the user."""
    """"'message_for_input' is kept just in case want to show message to the user. Can be ignored if not required."""

    user_string = input(
        message_for_input + "\nPlease enter the Morse code sequence here (leave blank & press Enter to terminate):")

    # Return the string(sequence) entered by user
    return user_string


def input_validation_function(user_input):
    """Method to perform various validations on user input. If error found, return with error message"""

    # Check if input is null?
    if user_input == "":
        return "Input is blank so terminated!"

    # Check if space within input?
    if " " in user_input:
        return "Error! Input contains a blank/space"

    # Check whether input contains only *
    if len(set(user_input)) == 1 and "*" in set(user_input):
        return "Error! Please enter characters among 1 &/or 0 separated by *"

    # Check if input contains either of 0, 1 or *
    if bool(re.match('[0-1*]', user_input)) is False:
        return "Error! Please enter characters among 1 &/or 0"

    # Check whether input has more than 3 asterisks?
    if "****" in user_input:
        return "Error! Incorrect number of * as separators"

    # Check if ** not in start or end of sequence
    if (user_input[0] == "*" and user_input[1] == "*" and user_input[2] != "*") or \
            (user_input[-1] == "*" and user_input[-2] == "*" and user_input[-3] != "*"):
        return "Error! Incorrect number of * as separators"

    # Check whether * at the start or end of sequence
    if (user_input[0] == "*" and user_input[1] != "*") or (user_input[-1] == "*" and user_input[-2] != "*"):
        return "Error! Incorrect number of * as separators"

    # Check if ** not anywhere in the sequence
    for each_char_index in range(1, len(user_input)-2):
        if user_input[each_char_index-1] != "*" and \
                user_input[each_char_index] == "*" and \
                user_input[each_char_index+1] == "*" and \
                user_input[each_char_index+2] != "*":
            return "Error! Incorrect use of * as separators"

    # Store the code for punctuations & set the flag
    punctuations = ["010101", "110011", "001100"]
    punctuation_flag = False

    # Check if sequence ends with either of the punctuations or not?
    for each_punctuation in punctuations:
        if user_input[-6:] == each_punctuation and punctuation_flag is False:
            punctuation_flag = True
    if punctuation_flag is False:
        return "Error! Input should end with a morse code for punctuation mark (,/./?)"

    # Check if input should not just a punctuation
    elif (len(user_input) == 6) and (user_input == "010101" or "110011" or "001100"):
        return "You've entered only the punctuation code! Please enter a word too"

    # If the length of input is less than 6, means no punctuation code is entered. So, show error accordingly
    elif len(user_input) <= 6:
        return "Error! Sentence should end with a morse code for punctuation mark"

    # # Check of presence of consecutive commas
    # if "110011*110011" in user_input:
    #     return "Warning! Morse code for , (110011) entered consecutively. Kindly re check and enter your sequence"

    # Check of presence of consecutive punctuations
    for each_punctuation_code_a in punctuations:
        for each_punctuation_code_b in punctuations:
            for each_separator_code in {"*", "***"}:
                if each_punctuation_code_a + each_separator_code + each_punctuation_code_b in user_input:
                    return "Error! Consecutive punctuations found. Kindly re check and enter your sequence"


def analysis_type_input_function():
    """Method to ask user which type of analysis is intended"""

    # Display the menu to user to select options from it
    analysis_type_input = input("\nWhich level of analysis is intended:\n" +
                                "\t1. Character count\n" +
                                "\t2. Word count\n" +
                                "\t3. Sentence type count\n" +
                                "\t4. Above all\n" +
                                "\t5. Exit(no analysis) from the whole execution\n"
                                "Please enter the serial number:")

    # Return the option that user has had selected
    return analysis_type_input


def main():

    # Create an object for Decode class
    decode_obj = Decoder()

    # Print the Morse code dictionary in readable format
    print(decode_obj)

    # Showing the instructions about how to enter input &/or terminate
    print("Instructions:\n-------------------------------------------------------------------------------------------\n"
          "Enter the word in Morse code(0/1) sequence(s) separated by \"*\" & \"***\" for space\n" +
          "Sentences should end with \".\"(clauses) or \",\"(complete sentences) or \"?\"(questions)\n" +
          "Eg.:'011*111*011*110011***00***0100*111*0001*0***0110*1011*1*0000*111*10*010101' for 'WOW, I LOVE PYTHON.'" +
          "\nLeave blank & press Enter to terminate.\n" +
          "-------------------------------------------------------------------------------------------")

    # Initialise variable that will hold the morse code sequences (user input)
    input_morse = []
    input_str = "garbage"  # Created to store random data so that it doesn't start as blank & enter while loop below it

    # While loop to keep asking user from inputs until user leaves blank to terminate.
    while input_str != "":

        # Take user input of morse code sequence
        input_str = input_function("")

        # If input is not blank, proceed for validation
        if input_str != "":

            # Check for validations if any. If error, then store the error message in a string
            validation_message = input_validation_function(input_str)

            # If 'validation_message' is none, means no error in input
            if validation_message is None:

                # Get the decoded string
                # Get the boolean if all codes match with the code in morse dictionary
                # Get the list if invalid codes by decoding user input morse code
                decoded_str, invalid_character_check, invalid_character_list = decode_obj.decode(input_str.split(" "))

                # Check the boolean variable which represents whether any invalid morse code in user input sequence
                if invalid_character_check is True:
                    print("Error! Invalid Morse code found", invalid_character_list, ". Kindly re check and enter")

                # If no kind of error in input, store the string in the list of multiple user inputs
                else:
                    input_morse.append(input_str)

            # Print the validation message if 'validation_message' is not none
            else:
                print(validation_message)

        # If user leaves the input blank, terminate input mode with a message
        else:
            print("Input is blank, so terminated!")

    # Show the list of all valid inputs
    # print("Valid inputs:", input_morse)

    # Initialise string that will contain the decoded text of user morse code input
    decoded_output = ""

    # If user has valid inputs then proceed with decoding & display the decoded string
    if len(input_morse) > 0:

        # Get the decoded string
        # Get the boolean if all codes match with the code in morse dictionary
        # Get the list if invalid codes by decoding user input morse code
        decoded_output, invalid_character_check, invalid_character_list = decode_obj.decode(input_morse)

        # Display decoded text
        print("\nDecoded output:\n================================================================================")
        for i in range(len(decoded_output)):
            print(decoded_output[i])
        print("================================================================================")

    # Initialised & stored random data so that it can enter in while loop below it
    user_input_analysis_type = "garbage"

    # While loop to take type of analysis input from user. Keep asking until valid answer
    while user_input_analysis_type not in {"1", "2", "3", "4", "5"}:

        # Take input of type of analysis required
        user_input_analysis_type = analysis_type_input_function()

        # If input is not valid, show appropriate message & ask again in while loop
        if user_input_analysis_type not in {"1", "2", "3", "4", "5"}:
            print("Please enter a valid response")

    # Create objects for classes - CharacterAnalyser(), WordAnalyser() & SentenceAnalyser()
    character_analyser_obj = CharacterAnalyser()
    word_analyser_obj = WordAnalyser()
    sentence_analyser_obj = SentenceAnalyser()

    # If user enters "1" meaning character analysis
    if user_input_analysis_type == "1":

        # run character analysing function using object & print the analysed output
        character_analyser_obj.analyse_characters(decoded_output)
        print(character_analyser_obj)

    # If user enters "2" meaning word analysis
    elif user_input_analysis_type == "2":

        # run word analysing function using object & print the analysed output
        word_analyser_obj.analyse_words(decoded_output)
        print(word_analyser_obj)

    # If user enters "3" meaning sentence analysis
    elif user_input_analysis_type == "3":

        # run sentence analysing function using object & print the analysed output
        sentence_analyser_obj.analyse_sentences(decoded_output)
        print(sentence_analyser_obj)

    # If user enters "4" meaning all types analysis (character, word & sentence)
    elif user_input_analysis_type == "4":

        # run all (character, word & sentence) analysing functions using respective object & print the analysed output
        character_analyser_obj.analyse_characters(decoded_output)
        print(character_analyser_obj)

        word_analyser_obj.analyse_words(decoded_output)
        print(word_analyser_obj)

        sentence_analyser_obj.analyse_sentences(decoded_output)
        print(sentence_analyser_obj)

    # If user enters 5, meaning exit from the code
    elif user_input_analysis_type == "5":
        print("\nThank you for using this script. Have a good time ahead!!")
        exit()


# Define that main() is the main function of the program
if __name__ == "__main__":
    main()
