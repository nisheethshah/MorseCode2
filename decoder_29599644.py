# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 29/04/2018
# Last Modified Date: 30/04/2018
# Assignment 2: Task 1: Building a class for Morse Code decoder
# -----------------------------------------------------------------------------

# Have created an Excel file with Morse Code key & values.
# We'll pull dictionary data from that Excel file.
# So I'll import that file into here as below -
import xlrd


class Decoder:

    # Creating a variable that can hold the Excel data. "xlrd.open_workbook" is used to fetch the Excel data.
    workbook = xlrd.open_workbook("Data.xlsx")

    # We'll save the keys & values in a list from Excel file first sheet(means '0').
    # For keys, we'll fetch data from first row in first column i.e programmatically, it means row 0, column 0.
    # & for values, we'll fetch data from row 0 onwards in column 1 (i.e. first row onwards in second column).
    key_list = workbook.sheet_by_index(0).col_values(0, 0)
    val_list = workbook.sheet_by_index(0).col_values(1, 0)

    def __init__(self):
        """Constructor for Morse code dictionary"""

        # Passing the pair of keys & values in the dictionary
        self.data_dictionary = {str(a).replace(".0", ""): b for a, b in zip(Decoder.key_list, Decoder.val_list)}

    def __str__(self):
        """Re-define this method to present the Morse code representation table in a readable format"""

        # Initialize variables
        data_dictionary_output = "\nEnglish character with it's Morse code:" + \
                                 "\n-------------------------------------------------\n"
        for key, value in self.data_dictionary.items():

            # Store the dictionary items in a string
            data_dictionary_output += str(key) + ":" + str(value) + "\n"

        # Return the string with dictionary data in readable format
        return data_dictionary_output

    def decode(self, morse_code_sequence):
        """Method that performs the decoding process"""

        # Initialize variables
        invalid_character = False
        invalid_character_list = []
        decoded_input = []

        # Iterate each line of multi line inputs from user
        for each_line in morse_code_sequence:

            # Split out each word of user input separated by ***
            each_word_split = each_line.split("***")

            # String variable to store decoded output for each line of morse code
            decode_string = ""

            # Iterate each word of each line of user input
            for each_char in each_word_split:

                # Split out each character of each word by *
                each_char_split = each_char.split("*")

                # Iterate each character from above split list
                for each_code in each_char_split:

                    # Check if each Morse code present in dictionary or not
                    if each_code in self.data_dictionary.values():

                        # if match found, extract the English corresponding character (key) from dictionary
                        decode_string += (
                            list(self.data_dictionary.keys())[list(self.data_dictionary.values()).index(each_code)])
                    else:
                        # Toggle the invalid flag & store the invalid character in another list
                        invalid_character = True
                        invalid_character_list.append(each_code)

                # Add space at the end of each word
                decode_string += " "

            # Remove the unnecessary space at the end from the string
            decode_string = decode_string[:-1]

            # Save the whole string as element in a list
            decoded_input.append(decode_string)

        return decoded_input, invalid_character, invalid_character_list
