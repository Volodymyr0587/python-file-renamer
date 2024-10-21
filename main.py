import os
import re
import string

def rename_files_in_folder(folder_path: str):

    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    # define counter for information display after process files
    file_counter = 0
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full path of the file
        full_path = os.path.join(folder_path, filename)
        # Check if it is file
        if os.path.isfile(full_path):
            file_counter += 1
            # Separate the file name and the extension
            name, ext = os.path.splitext(filename)
            # Process the name: lowercase, remove punctuation, replace whitespace with a dash
            new_name = re.sub('\s+', '-', name.translate(translator).strip().lower())

            # Form the new filename
            new_filename = f"{new_name}{ext.lower()}"

            # Construct the full paths
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

    result_text = "files" if (file_counter > 1 or file_counter == 0) else "file"
    print(f"\nDONE! {file_counter} {result_text} processed.")


if __name__ == "__main__":
    folder_path = input("Enter the path to the file folder: \n")
    rename_files_in_folder(folder_path)