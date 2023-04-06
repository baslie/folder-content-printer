# Folder Content Printer

A Python script that iterates through the specified directory, prints the content of files, and writes the output to a specified file. The content will be separated by tags for better readability.

## Usage

1. Set the `my_folder_path` variable to the folder path you want to list the content of.
2. Set the `my_output_file` variable to the path where you want to save the output file.
3. Run the script.

```python
my_folder_path = "C:\\Users\\Roman\\Desktop\\Chrome\\ChatGPT_Clipper_Extension"
my_output_file = "C:\\Users\\Roman\\Desktop\\output.txt"
```

## Example

Given a folder structure like this:

```
my_folder/
├─ file1.txt
├─ file2.py
├─ image1.jpg
└─ subfolder/
   ├─ file3.html
   └─ file4.json
```

After running the script, the `output.txt` file will contain the following:

```
- - - - - - - - - - - - - - - - - - - -

1. file1.txt
2. file2.py
3. image1.jpg
4. subfolder

- - - - - - - - - - - - - - - - - - - -

1. TXT-file "file1.txt"

[Content of file1.txt]

- - - - - - - - - - - - - - - - - - - -

2. PY-file "file2.py"

[Content of file2.py]

- - - - - - - - - - - - - - - - - - - -

3. image1.jpg

- - - - - - - - - - - - - - - - - - - -

4. Folder "subfolder"

- - - - - - - - - - - - - - - - - - - -

4.1. HTML-file "file3.html"

[Content of file3.html]

- - - - - - - - - - - - - - - - - - - -

4.2. JSON-file "file4.json"

[Content of file4.json]

- - - - - - - - - - - - - - - - - - - -
```

**Note:** The content of non-text files (images, archives, etc.) will not be included in the output file.
