import os

def read_notes(folder_path):
    notes_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            notes_list.append(filename)
    return notes_list

def create_note(folder_path, note_title, note_content):
    note_filename = f"{note_title}.txt"
    note_path = os.path.join(folder_path, note_filename)
    
    with open(note_path, 'w') as note_file:
        note_file.write(note_content)

def edit_note(folder_path, note_title):
    note_filename = f"{note_title}.txt"
    note_path = os.path.join(folder_path, note_filename)

    if os.path.exists(note_path):
        with open(note_path, 'r') as note_file:
            current_content = note_file.read()

        print(f"Current content of '{note_title}':")
        print(current_content)

        new_content = input("Enter the new content: ")

        with open(note_path, 'w') as note_file:
            note_file.write(new_content)
        print(f"Note '{note_title}' edited successfully.")
    else:
        print(f"Note '{note_title}' not found.")

def main():
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
            notes_list = read_notes(notes_folder_path)
            print("\nAvailable Notes:")
            for note in notes_list:
                print(note)
        elif choice == '2':
            note_title = input("Enter the title for the new note: ")
            note_content = input("Enter the content for the new note: ")
            create_note(notes_folder_path, note_title, note_content)
            print(f"Note '{note_title}' created successfully.")
        elif choice == '3':
            notes_list = read_notes(notes_folder_path)
            if notes_list:
                print("\nAvailable Notes:")
                for i, note in enumerate(notes_list, start=1):
                    print(f"{i}. {note}")

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
    main()
