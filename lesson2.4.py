
import os


migrations = "Migrations"
current_directory = os.path.dirname(os.path.abspath(__file__))
migration_abs_path = os.path.join(current_directory, migrations)
files_list = [f for f in os.listdir(migration_abs_path) if f.endswith('.sql')]

rekurs_files = []
user_input = input("Введите строку: ")
for file in files_list:
    with open(os.path.join(migration_abs_path, file), 'rt') as f:
        data_text = f.read()
        if user_input.lower() in data_text.lower():
            rekurs_files.append[file]

