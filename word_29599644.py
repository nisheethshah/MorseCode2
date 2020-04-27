# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 30/04/2018
# Last Modified Date: 30/04/2018
# Assignment 2: Task 3: Building a class for analysing decoded words
# -----------------------------------------------------------------------------


class WordAnalyser:

    def __init__(self):
        """Constructor to define and initialise the dictionary structure for words"""
        self.word_count_dictionary = dict()

    def __str__(self):
        """Method to present the number of occurrences for each word in a readable format"""

        # Initialize variables
        data_dictionary_output = "Frequency of each word:\n-------------------------------------------------\n"
        for key, value in self.word_count_dictionary.items():

            # Show only those words whose occurrence count is more than 0
            if value > 0:

                # Store the dictionary items in a string
                data_dictionary_output += str(key) + ":" + str(value) + "\n"

        return data_dictionary_output

    def analyse_words(self, decoded_sequence):
        """Count the occurrences for each word encountered in the given decoded sequence"""

        # Iterate each line of decoded sequence
        for each_line in decoded_sequence:

            # Ignore the punctuations at the end of words while counting the occurrence of each word
            each_line = each_line.replace(",", "").replace("?", "").replace(".", "")

            # Split each word on the basis of space between them
            each_word_split = each_line.split(" ")

            # Iterate each word
            for each_word in each_word_split:

                # If encountered a word for first time, store it & set its occurrence as 1
                if each_word not in self.word_count_dictionary.keys():
                    self.word_count_dictionary[each_word] = 1

                # If encountered the word earlier, increment its counter
                else:
                    self.word_count_dictionary[each_word] += 1
