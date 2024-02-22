import json
import os


class SavaLoadSystem():
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save(self, data, name):
        try:
            file_path = os.path.join(self.save_folder, name + self.file_extension)

            # Забезпечте, що каталог існує перед створенням файлу
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w') as data_file:
                json.dump(data, data_file)
        except Exception as e:
            print(f"Error saving file: {e}")

    def load(self, name, default_value=None):
        try:
            file_path = os.path.join(self.save_folder, name + self.file_extension)
            with open(file_path) as data_file:
                data = json.load(data_file)
                return data
        except FileNotFoundError:
            # Якщо файл не існує, повертаємо значення за замовчуванням
            print(f"File '{name}' not found. Returning the default value.")
            return default_value
