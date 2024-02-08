import os

def read_notes(folder_path):
    """
    This function takes a folder path as input and returns a list of all the .txt files in the folder.
    """
    notes_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            notes_list.append(filename)
    return notes_list

def read_note(folder_path, note_title):
    """
    This function takes a folder path and note title as input and returns the content of the specified note.
    """
    note_filename = f"{note_title}"
    note_path = os.path.join(folder_path, note_filename)

    with open(note_path, 'r') as note_file:
        note_content = note_file.read()
    return note_content
def console_editor():
    """
    This function allows the user to enter multiple lines of text in the console.
    The user can type 'END' on a new line to indicate the end of the text.
    """
    print("Enter the content (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

def create_note(folder_path, note_title, note_content):
    """
    This function takes a folder path, note title, and note content as input and creates a new .txt file with the note content in the specified folder.
    """
    note_filename = f"{note_title}.txt"
    note_path = os.path.join(folder_path, note_filename)
    note_content = console_editor()
    with open(note_path, 'w') as note_file:
        note_file.write(note_content)

def edit_note(folder_path, note_title):
    """
    This function takes a folder path and note title as input, reads the content of the specified note, allows the user to enter new content, and updates the note with the new content.
    """
    note_filename = f"{note_title}.txt"
    note_path = os.path.join(folder_path, note_filename)

    if os.path.exists(note_path):
        with open(note_path, 'r') as note_file:
            current_content = note_file.read()

        print(f"Current content of '{note_title}':")
        print(current_content)

        new_content = console_editor()
        with open(note_path, 'w') as note_file:
            note_file.write(new_content)

        print(f"Note '{note_title}' edited successfully.")
    else:
        print(f"Note '{note_title}' not found.")

#enumerate notes
def enumerate_notes(folder_path):
    print("\nAvailable Notes:")
    notes_list = read_notes(folder_path)
    for i, note in enumerate(notes_list, start=1):
        print(f"{i}. {note}")
    return notes_list


def main_notes():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    notes_folder_path = os.path.join(desktop_path, 'organization', 'notes')

    while True:
        print("\nNotes Manager Menu:")
        print("1. Read Notes")
        print("2. Create Note")
        print("3. Edit Note")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Read and display the list of notes
            notes_list = enumerate_notes(notes_folder_path)

            if not notes_list:
                print("No notes available.")
            else:
                note_number = int(input("Enter the number of the note to read: "))
                if 1 <= note_number <= len(notes_list):
                    note_to_read = notes_list[note_number - 1]
                    note_content = read_note(notes_folder_path, note_to_read)
                    print(f"\nContent of '{note_to_read}':\n{note_content}")
                else:
                    print("Invalid note number.")
        elif choice == '2':
            # Create a new note
            note_title = input("Enter the title for the new note: ")
            note_content = input("Enter the content for the new note: ")
            create_note(notes_folder_path, note_title, note_content)
            print(f"Note '{note_title}' created successfully.")
        elif choice == '3':
            # Edit an existing note
            notes_list = read_notes(notes_folder_path)
            if notes_list:
                enumerate_notes(notes_folder_path)
                note_number = int(input("Enter the number of the note to edit: "))
                if 1 <= note_number <= len(notes_list):
                    selected_note = notes_list[note_number - 1]
                    edit_note(notes_folder_path, selected_note[:-4])  # Remove ".txt" extension
                else:
                    print("Invalid note number.")
            else:
                print("No notes available to edit.")
        elif choice == '4':
            print("Exiting Notes Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_notes()
