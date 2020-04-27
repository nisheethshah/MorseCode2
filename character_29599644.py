# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 30/04/2018
# Last Modified Date: 30/04/2018
# Assignment 2: Task 2: Building a class for analysing decoded characters
# -----------------------------------------------------------------------------

# Importing Decode class to refer the structure of dictionary
from decoder_29599644 import Decoder


class CharacterAnalyser:

    def __init__(self):
        """Constructor to define and initialise the dictionary structure for characters occurrence"""
        self.char_count_dictionary = {str(a).replace(".0", ""): 0 for a, b in zip(Decoder.key_list, Decoder.val_list)}

    def __str__(self):
        """method to present the number of occurrences for each of the letters and numerals in a readable format"""

        # Initialize variables
        data_dictionary_output = "\nFrequency of each character:\n-------------------------------------------------\n"

        for key, value in self.char_count_dictionary.items():

            # Show only those characters whose occurrence count is more than 0
            if value > 0:

                # Store the dictionary items in a string
                data_dictionary_output += str(key) + ":" + str(value) + "\n"

        return data_dictionary_output

    def analyse_characters(self, decoded_sequence):
        """Count the occurrences for each of the letters and numerals encountered in the given decoded sequence"""

        # Iterate each line of decoded sequence
        for each_line in decoded_sequence:

            # Fetching each letter from the each sequence.
            for each_char in each_line:

                # Check whether each letter present in the list of keys in count dictionary.
                if each_char in self.char_count_dictionary.keys():

                    # Increment the occurrence of key's value by 1.
                    self.char_count_dictionary[each_char] += 1

        # As per assignment spec, we do not require to count occurrence of punctuations
        del self.char_count_dictionary[","]
        del self.char_count_dictionary["?"]
        del self.char_count_dictionary["."]
