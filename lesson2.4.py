"""Пользователь вводит поисковую информацию. Программа считывает эту информацию, ищет наличие этой информации в файлах
папки Migrations. Если находит их, то в заранее созданный пустой список дополняет файлами, названия которых совпали.
Далее выводим наименования файлов и их количество (len) в списке(который был до этого пустым)"""
import os


# put abspath for Migration directory
def get_abspath(directory_name="Migrations"):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    migration_abs_path = os.path.join(current_directory, directory_name)
    return migration_abs_path


# creating function of empty file list, that append with input data
def creating_file_list(input_info, files_list, migration_abs_path=get_abspath()):
    empty_file_list = []
    for file in files_list:
        with open(os.path.join(migration_abs_path, file), 'rt') as f:
            data = f.read()
            if input_info.lower() in data.lower():
                empty_file_list.append(file)
    return empty_file_list, len(empty_file_list)


# Main part
def core():
    migration_abs_path = get_abspath()
    files_list = [f for f in os.listdir(migration_abs_path) if f.endswith('.sql')]

    while True:
        search_info = input('Введите строку: ')
        file_list_info = creating_file_list(search_info, files_list, migration_abs_path)
        files_list, quantity = file_list_info # Здесь была ошибка (на этом этапе files_list должно было заменяться)
        for file in files_list:
            print(file)
        print('Всего: {0}'.format(quantity))


core()

