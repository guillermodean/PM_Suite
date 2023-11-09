import os
import shutil
import getpass


def create_secrets_folder():
    # Create the 'secrets' folder if it doesn't exist
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    organization_path = os.path.join(desktop_path, 'organization')
    secrets_folder_path = os.path.join(organization_path, 'secrets')

    if not os.path.exists(secrets_folder_path):
        os.makedirs(secrets_folder_path)
        print(f"Created 'secrets' folder at {secrets_folder_path}")

def organize_desktop():
    
    create_secrets_folder()
    # Get the desktop path for the active user on Windows
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # Create the organization folder if it doesn't exist
    organization_path = os.path.join(desktop_path, 'organization')
    if not os.path.exists(organization_path):
        os.makedirs(organization_path)
        print(f"Created organization folder at {organization_path}")

    # List all files on the desktop
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    # Define file types and corresponding folders
    file_types = {
        'Word Documents': ['.doc', '.docx'],
        'Excel Spreadsheets': ['.xls', '.xlsx'],
        'PDFs': ['.pdf'],
        'Images': ['.png', '.jpg', '.jpeg', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Powerpoint':['.pptx','.ppts']
    }

    # Organize files into folders
    for file in files:
        file_type = os.path.splitext(file)[1].lower()

        # Find the corresponding folder for the file type
        for folder, extensions in file_types.items():
            if file_type in extensions:
                # Special handling for Word and Excel documents
                if folder in ['Word Documents', 'Excel Spreadsheets']:
                    office_type = 'Word' if file_type == '.docx' else 'Excel' if file_type == '.xlsx' else 'Other'
                    dest_folder = os.path.join(organization_path, folder, office_type)
                else:
                    dest_folder = os.path.join(organization_path, folder)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.move(os.path.join(desktop_path, file), os.path.join(dest_folder, file))
                print(f"Moved {file} to {dest_folder}")
                break
        else:
            # If the file type doesn't match any predefined types, skip it
            print(f"Ignored {file} (no matching category)")

    print("Desktop organization completed.")

def list_organization_folder():
    # Get the desktop path for the active user on Windows
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # Check if the organization folder exists
    organization_path = os.path.join(desktop_path, 'organization')
    if not os.path.exists(organization_path):
        print("Organization folder not found.")
        return

    # List the contents of the organization folder
    print("Contents of the organization folder:")
    for root, dirs, files in os.walk(organization_path):
        for file in files:
            print(os.path.join(root, file))

def list_organization_folder():
    # Get the desktop path for the active user on Windows
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # Check if the organization folder exists
    organization_path = os.path.join(desktop_path, 'organization')
    if not os.path.exists(organization_path):
        print("Organization folder not found.")
        return

    # List the contents of the organization folder
    print("Contents of the organization folder:")
    for root, dirs, files in os.walk(organization_path):
        for file in files:
            print(os.path.join(root, file))
        for directory in dirs:
            print(os.path.join(root, directory))

if __name__ == "__main__":
    organize_desktop()