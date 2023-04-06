import os
from pathlib import Path

my_folder_path = "C:\\YOUR\\PATH\\TO\\FOLDER\\my_folder"
my_output_file = "C:\\YOUR\\PATH\\TO\\OUTPUT\\output.txt"

TEXT_EXTENSIONS = {".txt", ".html", ".js", ".css", ".py", ".json"}
OTHER_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".zip", ".rar", ".tar", ".gz", ".7z"}

def print_folder_content(path: str, output_file: str):
    def list_files_and_folders(folder_path, prefix=""):
        content = sorted(os.listdir(folder_path))
        for idx, item in enumerate(content, 1):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                result.append(f"{prefix}{idx}. {item}")
                file_content.append((f"{prefix}{idx}", item_path, "folder"))
                list_files_and_folders(item_path, f"{prefix}{idx}.")
            else:
                result.append(f"{prefix}{idx}. {item}")
                if Path(item).suffix in TEXT_EXTENSIONS | OTHER_EXTENSIONS:
                    file_content.append((f"{prefix}{idx}", item_path, "file"))

    result = []
    file_content = []
    list_files_and_folders(path)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("- - - - - - - - - - - - - - - - - - - -\n\n")
        f.write("\n".join(result))
        f.write("\n\n- - - - - - - - - - - - - - - - - - - -\n\n")

        for idx, item_path, item_type in file_content:
            if item_type == "folder":
                f.write(f"{idx}. Папка \"{os.path.basename(item_path)}\"\n\n")
                f.write("- - - - - - - - - - - - - - - - - - - -\n\n")
            else:
                ext = Path(item_path).suffix
                if ext in TEXT_EXTENSIONS:
                    f.write(f"{idx}. {ext.upper()[1:]}-файл \"{os.path.basename(item_path)}\"\n\n")
                    with open(item_path, "r", encoding="utf-8") as file:
                        f.write(file.read())
                elif ext in OTHER_EXTENSIONS:
                    f.write(f"{idx}. {os.path.basename(item_path)}")
                f.write("\n\n- - - - - - - - - - - - - - - - - - - -\n\n")

if __name__ == "__main__":
    print_folder_content(my_folder_path, my_output_file)
