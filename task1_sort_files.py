import os
import shutil
import argparse

def sort_and_copy_files(src_dir, dest_dir='dist'):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            full_path = os.path.join(src_dir, item)

            if os.path.isdir(full_path):
                sort_and_copy_files(full_path, dest_dir)
            elif os.path.isfile(full_path):
                try:
                    file_ext = os.path.splitext(item)[1].lstrip('.').lower() or "no_extension"
                    ext_dir = os.path.join(dest_dir, file_ext)

                    if not os.path.exists(ext_dir):
                        os.makedirs(ext_dir)

                    shutil.copy2(full_path, ext_dir)
                except Exception as copy_err:
                    print(f"[ERROR] Не вдалося скопіювати файл {full_path}: {copy_err}")
    except Exception as dir_err:
        print(f"[ERROR] Не вдалося обробити директорію {src_dir}: {dir_err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    sort_and_copy_files(args.src, args.dest)
    print(f" Файли успішно скопійовані та відсортовані у '{args.dest}'")
