import sys 
import os 

# --- Configuration ---
INPUT_FILENAME = "input_data.txt"
OUTPUT_FILENAME = "modified_output.txt"
MODIFICATION_BANNER = "\n\n--- 🌟 GEMINI'S DRAMATIC REWRITE 🌟 ---\n\n"
MODIFICATION_FOOTER = "\n\n--- 🎬 END OF TRANSMISSION 🎬 ---\n"


def process_file_challenge(): 
    """
    Prompts the user for a filename, reads its contents, modifies it
    (by converting to uppercase and adding a banner), and writes the
    result to a new file.

    Includes robust error handling for file not found and general I/O issues.
    """
    print("✨ Welcome to the File I/O & Error Handling Lab! ✨")
    print(f"We are trying to read a file, modify it, and write the result to '{OUTPUT_FILENAME}'.")
    print("-" * 40) 

    # 1. Ask the user for the filename
    # We use a default suggestion, but the user can enter anything.
    input_file_name = input(f"Enter the input filename (e.g., '{INPUT_FILENAME}'): ").strip()

    if not input_file_name:
        print("🛑 Input cannot be empty. Defaulting to 'input_data.txt'.")
        input_file_name = INPUT_FILENAME

    file_content = ""

    # 2. File Read Challenge: Handle potential errors during reading
    try:
        print(f"\nAttempting to read from: '{input_file_name}'...")
        # Use 'with open' for automatic file closing, even if errors occur.
        with open(input_file_name, 'r', encoding='utf-8') as file_in:
            file_content = file_in.read()
            print("✅ File read successful!")

    except FileNotFoundError:
        # Specific handling for the file not being found (Error Handling Lab)
        print(f"\n❌ ERROR: File not found. The file '{input_file_name}' does not exist.")
        print("Tip: Make sure the file is in the same directory as this script.")
        return # Exit the function if the read failed.

    except IOError as e:
        # General I/O error handling (e.g., permission denied, disk full)
        print(f"\n❌ ERROR: An I/O error occurred while reading the file: {e}")
        return

    except Exception as e:
        # Catch any unexpected errors
        print(f"\n❌ UNEXPECTED ERROR during file read: {e}")
        return

    # 3. Modify Content
    modified_content = file_content.upper()
    modified_content = MODIFICATION_BANNER + modified_content + MODIFICATION_FOOTER
    print(f"🎉 Content modified! ({len(file_content)} chars -> {len(modified_content)} chars)")


    # 4. File Write Challenge: Write modified content to the new file
    try:
        print(f"Attempting to write to: '{OUTPUT_FILENAME}'...")
        # 'w' mode truncates the file if it exists or creates it if it doesn't.
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file_out:
            file_out.write(modified_content)
            # Displaying the file path for easy access
            print(f"✅ Success! Modified content saved to '{os.path.abspath(OUTPUT_FILENAME)}'")

    except IOError as e:
        # Handle errors during the writing process
        print(f"\n❌ ERROR: Could not write to file '{OUTPUT_FILENAME}'. Check permissions. Details: {e}")

    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR during file write: {e}")


if __name__ == "__main__":
    # To test this, make sure you create a file named 'input_data.txt'
    # with some text in it before running the script!
    process_file_challenge()
