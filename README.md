# File_Processor
File Handling &amp; Exception Handling
So, this Python script (file_processor.py) is basically here to let us show off our file I/O and error handling skills! It's designed to grab content from an existing text file, give it a dramatic, uppercase makeover (complete with a signature banner), and save the results to a new file.

The main vibe? No crash landings allowed. We handle file-not-found errors gracefully.

Features
Secure File Reading: Uses robust try...except blocks to handle potential FileNotFoundError (for when you forget where you saved that doc) and general IOError.

The Upper-Case Glow-Up: Converts all input text to scream-worthy UPPERCASE.

Dramatic Flair: Inserts the iconic GEMINI'S DRAMATIC REWRITE banner and an END OF TRANSMISSION footer around the modified content.

New File, Who Dis? Writes the finalized content to modified_output.txt.

Setup and Usage
Prerequisites

You just need Python 3. That's it.

Step 1: Create the Input File

For a successful run, you need to create a text file that the script can read.

Create a new file in the same directory as file_processor.py.

Name it input_data.txt (this is the script's default).

Add some text to it! (E.g., "Error handling is a vibe. I'm ready for my close-up.")

Step 2: Run the Script

Execute the script from your terminal:

python file_processor.py


Step 3: Input Filename

The script will prompt you: Enter the input filename (e.g., 'input_data.txt'):

Enter input_data.txt for a SUCCESSFUL run.

The output will be saved to modified_output.txt.

Testing the Error Handling (The Lab)
The core challenge of this script is handling the flop! Here's how to test the error handling:

Run the script again: python file_processor.py

When prompted for the filename, enter a file name that does not exist, such as: missing_file.txt

The script will catch the FileNotFoundError and print a helpful message, exiting cleanly without crashing:

ERROR: File not found. The file 'missing_file.txt' does not exist.
Tip: Make sure the file is in the same directory as this script.
