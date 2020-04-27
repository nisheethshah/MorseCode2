# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 30/05/2018
# Last Modified Date: 01/05/2018
# Assignment 2: Task 4: Building a class for analysing decoded sentences
# -----------------------------------------------------------------------------


class SentenceAnalyser:

    # Defining class variable for further uses in multiple functions
    sentence_types = ["clauses", "complete_sentences", "questions"]

    def __init__(self):
        """"Constructor to define and initialise the dictionary structure for sentence types"""
        # Initialize variables
        self.sentence_count_dictionary = dict()

        # Set the count of each sentence type as 0
        for each_type_of_sentence in SentenceAnalyser.sentence_types:
            self.sentence_count_dictionary[each_type_of_sentence] = 0

    def __str__(self):
        """Method to present the number of occurrences for each sentence type in a readable format"""

        # Initialize variables
        data_dictionary_output = "Frequency of each sentence:\n-------------------------------------------------\n"

        for key, value in self.sentence_count_dictionary.items():

            display_name = "garbage"

            if key == "clauses":
                display_name = "Clauses"
            elif key == "complete_sentences":
                display_name = "Complete Sentences"
            elif key == "questions":
                display_name = "Questions"

            # Store the dictionary items in a string
            data_dictionary_output += str(display_name) + ":" + str(value) + "\n"

        return data_dictionary_output

    def analyse_sentences(self, decoded_sequence):
        """Count the occurrences for each sentence type (number of clauses and/or a full sentence or a question)"""

        # Iterate each sequence in decoded output
        for each_line in decoded_sequence:

            # Iterate each sentence type from Class variable
            for each_type_of_sentence in SentenceAnalyser.sentence_types:

                # Initialize by garbage value
                splitter = "garbage"

                # Define the type of character that explains each sentence
                if each_type_of_sentence == "clauses":
                    splitter = ","
                elif each_type_of_sentence == "complete_sentences":
                    splitter = "."
                elif each_type_of_sentence == "questions":
                    splitter = "?"

                # Count the number of character of each sentence type
                self.sentence_count_dictionary[each_type_of_sentence] += each_line.count(splitter)
