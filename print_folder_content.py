import os
from pathlib import Path

# Наборы расширений, по которым распознаём текстовые и другие файлы
# ...
# Текстовые/кодовые файлы
TEXT_EXTENSIONS = {
    ".txt", ".html", ".js", ".css", ".py", ".json", ".gitignore", ".md", 
    ".env", ".yml", ".bat", ".ts", ".tsx", ".jsx", ".vue",   # JS/TS экосистема
    ".php", ".rb", ".sh", ".ps1", ".pl",                    # скрипты
    ".c", ".cpp", ".h", ".hpp", ".cs",                      # C, C++, C#
    ".java", ".kt", ".kts",                                 # Java/Kotlin
    ".go", ".rs", ".swift",                                 # Go, Rust, Swift
    ".sql",                                                 # SQL-скрипты
    # И т.д. — можно расширить по потребностям
}
# Другие (чаще бинарные/архивы/изображения), которые не нужно печатать
OTHER_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",  # картинки
    ".zip", ".rar", ".tar", ".gz", ".7z",             # архивы
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",         # офисные файлы
    ".exe", ".dll", ".so", ".dylib",                  # исполняемые/библиотеки
    # И т.д. — по необходимости проекта
}

def print_folder_content(folder_path: str, output_file: str):
    """
    Рекурсивно обходит папку 'folder_path' и записывает результат в 'output_file'.
    """

    def list_files_and_folders(current_path, prefix="", depth=0):
        items_in_folder = sorted(os.listdir(current_path))
        for idx, item in enumerate(items_in_folder, start=1):
            item_path = os.path.join(current_path, item)
            # Формируем отступы и символы ├──/└──
            indent = "    " * depth + ("├── " if idx < len(items_in_folder) else "└── ")

            if os.path.isdir(item_path):
                result_structure.append(f"{indent}{item}")
                file_content.append((f"{prefix}{idx}", item_path, "folder"))
                # Рекурсия для подпапок
                list_files_and_folders(item_path, f"{prefix}{idx}.", depth + 1)
            else:
                result_structure.append(f"{indent}{item}")
                ext = Path(item).suffix or f".{item}"
                # Запоминаем файлы только с нужными расширениями или скрытые (начинаются с точки)
                if ext in (TEXT_EXTENSIONS | OTHER_EXTENSIONS) or item.startswith("."):
                    file_content.append((f"{prefix}{idx}", item_path, "file"))

    # Здесь будет "дерево" папок/файлов и их индексы
    result_structure = []
    file_content = []

    # Запишем название корневой папки
    root_folder_name = os.path.basename(os.path.normpath(folder_path))
    result_structure.append(root_folder_name + "/")

    # Собираем инфу о вложениях
    list_files_and_folders(folder_path)

    # Записываем результат в файл
    with open(output_file, "w", encoding="utf-8") as f:
        # Сначала само "дерево" папки
        f.write("\n".join(result_structure))
        f.write("\n\n---\n\n")

        # Затем детали по файлам
        for idx, item_path, item_type in file_content:
            # Для вложенных папок пишем только их структуру, без содержимого
            if item_type == "folder":
                continue
            else:
                ext = Path(item_path).suffix or f".{Path(item_path).name}"
                filename = os.path.basename(item_path)

                # Если файл в списке текстовых расширений, печатаем его содержимое
                if ext in TEXT_EXTENSIONS or item_path.endswith(".gitignore"):
                    f.write(f"{idx}. {ext.upper()[1:]}-file \"{filename}\"\n\n")
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

                # Для остальных расширений выводим только имя
                elif ext in OTHER_EXTENSIONS:
                    f.write(f"{idx}. {filename}\n\n")


def main():
    # Определяем путь к текущему скрипту (папка «Code»)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Перебираем все элементы в «Code», ищем подпапки, и для каждой создаём отдельный txt-файл
    for item in os.listdir(script_dir):
        item_path = os.path.join(script_dir, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            # Заменяем пробелы на подчёркивания в названии выходного файла
            folder_name_for_file = item.replace(" ", "_")
            output_filename = f"{folder_name_for_file}_output.txt"
            output_path = os.path.join(script_dir, output_filename)

            # Печатаем структуру подпапки в соответствующий txt-файл
            print_folder_content(item_path, output_path)

if __name__ == "__main__":
    main()
