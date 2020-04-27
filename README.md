Introduction
	As we have seen in the first assignment, the current International Morse Code system encodes a range of characters, including the ISO basic Latin alphabets (A–Z), some additional Latin letter representing accents, the Arabic numerals (0–9), and a small set of punctuations and procedural signals (known as prosigns).
	In this assignment, we are going to adopt the same set of representation for the Morse Code used in the first assignment based on the binary digits. The ‘dots’ are represented by the digit 0 and the ‘dashes’ are represented by the digit 1. As for the spaces, they are represented by the character ‘*’.
 
	Our representation of Morse Code encodes the standard 26 letters (i.e. ‘A’ to ‘Z) and the 10 numerals (i.e. ‘0’ to ‘9’), with three additional punctuation characters (i.e. the period ‘.’; the comma ‘,’; and the question mark ‘?’).
	This assignment has 5 tasks which defines different functionalities as described further in this document.
	This project is created using PyCharm IDE using Anaconda.
 
Task 1
This file contains a class that serves as the Morse Code decoder. It has a class which includes a one instance variable which is a dictionary structure that represents each of the Morse Code characters as a string sequence of binary digits (0 and 1). This decoder class is used for decoding any Morse Code sequences.

Creating Morse code dictionary from Excel file:
The data dictionary is made from Excel file with keys & value in two columns. By importing “xlrd”, we can read the Excel file (Data.xlsx) in Python & read data from within it.
    
Creating an Excel file helps to easily modify/insert/delete the Morse code dictionary without touching the program (probably useful for someone with no or less programming knowledge). After pulling the dictionary, I have just displayed the dictionary as it is in the Task 1 output.

Decode user input:
The decode() function in this class is used to translate Morse sequence to English. We simply check each code from the user input with value from our dictionary. If they match, we can identify the English character by referring the value’s key in the dictionary. This way, we build & return the English sequence. Besides is the snippet of code where we check the Morse code with English characters in the dictionary & build the English sequence.
Task 2
This file defines a class for analysing the number of occurrences for each of the letters (i.e. ‘A’ to ‘Z) and numerals (i.e. ‘0’ to ‘9’) from the decoded sequences. This class should have one instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each of the letters and numerals decoded by the Morse Code decoder in Task 1. 

Character count dictionary:
We create a new dictionary with English characters as keys & its occurrence as values. The values are initialised with 0 within the constructor of this task file – 
 

Count the occurrence of each character:
	The decoded list is passed as a parameter in the function. This function is used to count the occurrence of each character from all the sequences in the list. If a character is found, the count is incremented in the dictionary.
 

Print the occurrence of each character:
	The occurrence of each character is printed in readable format using the function “__str__(self)”.

In above screenshot, only the characters are displayed whose occurrence is 1 or more.
Task 3
This file defines a class for analysing the number of occurrences for each of the English words from the decoded sequences. This class have one instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each word decoded by the Morse Code decoder in Task 1. 

Word count dictionary:
We create a new blank dictionary where we’ll store English words as keys & its occurrence as values. Initially the dictionary will contain no keys or values because we would not know what words user will enter – 
 

Count the occurrence of each word:
	The decoded list is passed as a parameter in the function. This function is used to count the occurrence of each words from all the sequences in the list. If a word shows up first time in the sequence, it will not be present in the dictionary. Therefore, we add that word in the dictionary & increment its count by 1. And if a word is repeated, it will be present in the dictionary; so, in this case, we’ll increment its value by 1.
 

Print the occurrence of each word:
	The occurrence of each word is printed in readable format using the function “__str__(self)”.
In the screenshot besides, only the characters are displayed whose occurrence is 1 or more. And the remaining characters whose occurrence is 0 is not shown in the output. This helps increase the readability of occurrences of each character. 
Task 4
This file defines a class for analysing the number of occurrences for each type of English sentences from the decoded sequences. This class should have one instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each type of sentences decoded by the Morse Code decoder in Task 1.
The types of sentence that we are handling include: clauses (indicated by the comma), complete sentences (indicated by the period), and questions (indicated by the question mark). 

Dictionary for count of sentence type:
We create a new dictionary with sentence type as keys & its occurrence as values. The values are initialised with 0 within the constructor of this task file – 
 

Count the occurrence of each sentence type:
	The decoded list is passed as a parameter in the function. This function is used to count the occurrences for each sentence type (which could be a number of clauses and/or a full sentence or a question) encountered in the given decoded sequence. The counts should be updated in the dictionary structure defined in the constructor.
 

Print the occurrence of each word:
	Occurrence of each sentence is printed in readable format using the function “__str__(self)”, similar to Task 2 & 3.
 
Task 5
This file has the main function that will drive the flow of execution of the program. The file also has other functions for taking input from user, check for validations in input Morse code & take the input for type of analysis required.

Flow of the main function:
-	Show Morse code dictionary (by Task 1 object)
-	Take Morse code input from the user & perform validations on it. Show appropriate error if input is incorrect.
-	Decode the Morse code (by Task 1 object)
-	Show user menu of the type of analysis required. And collect input for the same.
-	Show analysis (character/word/sentence count) based on the option selected in above step (by objects of Task 2/ Task 3/ Task 4).

Methods in this file & its purpose – 
1.	“input_function(message_for_input)”: This function is used to take Morse code input from the user & return the string.
2.	“input_validation_function(user_input)”: After user has entered the input, it needs to be checked whether is it correct or not i.e. the input should contain any out of “1” / “0” / “*”. There are also validation checks made viz. the input should end with a punctuation, should not contain alphabets, should not contain “**” or more than 3 asterisks, etc.
3.	“analysis_type_input_function()”: Show the menu of types of analysis a user would like to have. Followed by taking input code of analysis type.
4.	“main()”: This is the primary function wherein above functions are called. This function is used to define the flow of the program.

Usage of objects:
	Objects for each class is created in the main function. These objects helps to store an instance of the class. Other functions that are created in this file are called in main function as required. Other functions are created to redundancy of codes in main function.
	Input Morse codes & decoded output is passed among various classes through objects. Below is screenshot of snippet for creating an object for Task 1 inside main function –
  
Run Manual
To run the program efficiently – 
	This program is executed in PyCharm IDE using Anaconda for compiling Python.
	Run “main_29599644” file. As we have defined “main()” as main function of the program, Python will automatically search “main()” function in that file & run it. 
 
	User need to enter the Morse code in the input section. Various types of validations are handled in the program so if the user enters incorrect input (other than 1/0/*), then the program will display an error message to user. The message will be according to the type of error that has occurred.
	User can enter multiple sequences. As stated above, it a sequence is incorrect, it will be ignored with an error message & user will be prompted again for another input sequence.
	Once user is finished entering the all the sequences, then leave the input section blank press Enter to terminate the input process.
	Program will display the decoded sequences of all the valid inputs.
	After displaying the decoded sequences, program will prompt user to select the type of analysis required on decoded output – 
 
	User needs to enter the serial code among 1 to 4 for any of the type of analysis. Or enter 5 if want to exit the whole program.
	The program will show the type of analysis as desired by the user as per entered code. Let’s say, user enters 4. Program will display all types of analysis i.e. character count, word count & sentence count.
	And then the program will exit.
	

 
Sample Output
   
 
 
 
References
•	Stackoverflow.com. Python Creating Dictionary from excel data. Referred from https://stackoverflow.com/questions/14196013/python-creating-dictionary-from-excel-data?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa (Accessed 23/03/2018)
•	SiHa (Last edited Oct 6 '16 at 7:11), CrazyCasta. Stackoverflow.com. Check if string matches pattern. Retrieved from https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern/12595533?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
•	Python Reference Manual. Function definitions. Referred ‘how to return data from functions’ from https://docs.python.org/2.0/ref/function.html
•	Community♦ (Last edited May 23 '17 at 12:02), Stênio Elson. Stackoverflow.com. Get key by value in dictionary. Referred from https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
