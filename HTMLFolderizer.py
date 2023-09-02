import os
import shutil

def process_files(file_type):
    source_folder = "html_0"  # Ganti dengan path folder asal Anda

    for filename in os.listdir(source_folder):
        if filename.endswith(file_type):
            # Membuat nama folder baru berdasarkan nama file
            new_folder_name = filename.replace(file_type, "")

            # Membuat folder baru
            new_folder_path = os.path.join(source_folder, new_folder_name)
            os.makedirs(new_folder_path, exist_ok=True)

            # Memindahkan file ke folder baru
            old_file_path = os.path.join(source_folder, filename)
            new_file_path = os.path.join(new_folder_path, f"index{file_type}")
            shutil.move(old_file_path, new_file_path)

if __name__ == "__main__":
    file_type = input("Masukkan jenis file yang ingin diproses (html/php): ").strip()
    
    if file_type == "html":
        process_files(".html")
    elif file_type == "php":
        process_files(".php")
    else:
        print("Jenis file tidak dikenali. Harap masukkan 'html' atau 'php'.")
