import os
from pathlib import Path

my_folder_path = "C:\\YOUR\\PATH\\TO\\FOLDER\\my_folder"
my_output_file = "C:\\YOUR\\PATH\\TO\\OUTPUT\\output.txt"

TEXT_EXTENSIONS = {
    ".txt",
    ".html",
    ".js",
    ".css",
    ".py",
    ".json",
    ".gitignore",
    ".md",
    ".env",
    ".yml"
}
OTHER_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".zip",
    ".rar",
    ".tar",
    ".gz",
    ".7z"
}

def print_folder_content(path: str, output_file: str):
    def list_files_and_folders(folder_path, prefix="", depth=0):
        content = sorted(os.listdir(folder_path))
        for idx, item in enumerate(content, 1):
            item_path = os.path.join(folder_path, item)
            indent = "    " * depth + ("├── " if idx < len(content) else "└── ")
            if os.path.isdir(item_path):
                result.append(f"{indent}{item}")
                file_content.append((f"{prefix}{idx}", item_path, "folder"))
                list_files_and_folders(item_path, f"{prefix}{idx}.", depth + 1)
            else:
                result.append(f"{indent}{item}")
                ext = Path(item).suffix  
                if ext == "" or ext in (TEXT_EXTENSIONS | OTHER_EXTENSIONS) or item.startswith("."):
                    file_content.append((f"{prefix}{idx}", item_path, "file"))

    result = []
    file_content = []
    root_folder_name = os.path.basename(os.path.normpath(path))
    result.append(root_folder_name + "/")
    list_files_and_folders(path)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(result))
        f.write("\n\n---\n\n")

        for idx, item_path, item_type in file_content:
            if item_type == "folder":
                continue
            else:
                raw_ext = Path(item_path).suffix
                filename = os.path.basename(item_path)
                if raw_ext == "":
                    ext_print = "TXT"
                else:
                    ext_print = raw_ext.upper()[1:]

                if raw_ext == "" or raw_ext in TEXT_EXTENSIONS or item_path.endswith(".gitignore"):
                    f.write(f"{idx}. {ext_print}-file \"{filename}\"\n\n")
                    f.write(f"<\"{filename}\">\n")
                    try:
                        with open(item_path, "r", encoding="utf-8") as file:
                            content = file.read()
                            if not content.strip():
                                f.write("[File is empty]\n")
                            else:
                                f.write(content)
                    except Exception as e:
                        f.write(f"[Error reading file: {e}]\n")
                    f.write(f"\n</\"{filename}\">\n\n")
                elif raw_ext in OTHER_EXTENSIONS:
                    f.write(f"{idx}. {filename}\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    print_folder_content(my_folder_path, my_output_file)
