import json


class SavaLoadSystem():
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save(self, data, name):
        with open(self.save_folder + "/" + name + self.file_extension, 'w') as data_file:
            json.dump(data, data_file)

    def load(self, name):
        with open(self.save_folder + "/" + name + self.file_extension) as data_file:
            data = json.load(data_file)
