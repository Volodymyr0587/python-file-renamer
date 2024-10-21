# File Renamer Script

This Python script renames all files in a specified folder by converting all characters to lowercase, removing punctuation (except for file extensions), and replacing spaces with dashes (`-`).

## Features

- Converts all characters in the file name to **lowercase**.
- Removes **punctuation** from the file name (punctuation within the file extension remains intact).
- Replaces **whitespace** with a dash (`-`).
- Processes all files in a given folder and provides a summary of the number of files renamed.

## Prerequisites

- **Python 3.x** installed on your machine.
- The following Python standard libraries are used:
  - `os`
  - `re`
  - `string`

No additional external dependencies are required.

## How to Use

1. **Clone or download the script** to your local machine.
2. **Open a terminal** or command prompt.
3. Navigate to the folder where the script is located.
4. Run the script with Python:

   ```bash
   python main.py
   ```
5. When prompted, enter the path to the folder where your files are located.
6. The script will process all files in the folder, renaming them according to the specified rules.
7. After processing, the script will display the number of files renamed.

## Example

Suppose your folder contains the following files:
```
My File.txt
Another File!.pdf
special_case--File   .doc
```
After running the script, they will be renamed to:
```
my-file.txt
another-file.pdf
special-case-file.doc
```

## Notes

- This script only processes files and ignores directories.
- File extensions are preserved but converted to lowercase.
- The script will print the changes made for each file.

## License

This script is free to use and modify.
