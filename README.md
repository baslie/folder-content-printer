# Folder Content Printer

A Python script that iterates through the specified directory, prints the content of files, and writes the output to a specified file. The content will be separated by tags for better readability.

## Usage

1. Set the `my_folder_path` variable to the folder path you want to list the content of.
2. Set the `my_output_file` variable to the path where you want to save the output file.
3. Run the script.

```python
my_folder_path = "C:\\YOUR\\PATH\\TO\\FOLDER\\my_folder"
my_output_file = "C:\\YOUR\\PATH\\TO\\OUTPUT\\output.txt"
```

## Example

Given a folder structure like this:

```
my_folder/
└─ subfolder/
   ├─ file1.html
   └─ file2.json
├─ file3.txt
├─ file4.py
├─ imagejpg
```

After running the script, the `output.txt` file will contain the following:

```
- - - - - - - - - - - - - - - - - - - -

1. subfolder
1.1. file1.html
1.2. file2.json
2. file3.txt
3. file4.py
4. image.jpg

- - - - - - - - - - - - - - - - - - - -

1. Folder "subfolder"

- - - - - - - - - - - - - - - - - - - -

1.1. HTML-file "file1.html"

[Content of file1.html]

- - - - - - - - - - - - - - - - - - - -

1.2. JSON-file "file2.json"

[Content of file2.json]

- - - - - - - - - - - - - - - - - - - -

2. TXT-file "file3.txt"

[Content of file3.txt]

- - - - - - - - - - - - - - - - - - - -

3. PY-file "file4.py"

[Content of file4.py]

- - - - - - - - - - - - - - - - - - - -

4. image.jpg

- - - - - - - - - - - - - - - - - - - -
```

**Note:** The content of non-text files (images, archives, etc.) will not be included in the output file.
