import re
from contants import EXISTING_USERS_PATH, OPEN_FILE_MODES, DIVIDER_IN_FILES, DATABASE_FOLDER_PATH, TXT_FILETYPE


class User:
    def __init__(self, name):
        self.name = name
        self.container = set()
        self.check_container_existing()

    def check_container_existing(self):
        with open(EXISTING_USERS_PATH, OPEN_FILE_MODES.get("read")) as file:
            data = file.read()
            users_list = data.split(DIVIDER_IN_FILES)

            if self.name in users_list:
                self.load(self.name)

    def add(self, keys_list):
        self.container.update(keys_list)

    def remove(self, key):
        self.container.discard(key)

    def find(self, keys_list):
        found_keys = [key for key in keys_list if key in self.container]
        return found_keys

    def list(self):
        return self.container

    def grep(self, regexp):
        matched_keys = [key for key in self.container if bool(re.search(regexp, key))]
        return matched_keys

    def save(self):
        # Save users list
        with open(EXISTING_USERS_PATH, OPEN_FILE_MODES.get("read")) as file:
            data = file.read()
            users_set = set(data.split(DIVIDER_IN_FILES))
        users_set.add(self.name)
        with open(EXISTING_USERS_PATH, OPEN_FILE_MODES.get("write")) as file:
            data = DIVIDER_IN_FILES.join(list(users_set))
            file.write(data)
        # Save user info
        data = DIVIDER_IN_FILES.join(self.container)
        file_path = DATABASE_FOLDER_PATH + self.name + TXT_FILETYPE
        with open(file_path, OPEN_FILE_MODES.get("write")) as file:
            file.write(data)

    def load(self, username):
        file_path = DATABASE_FOLDER_PATH + username + TXT_FILETYPE
        with open(file_path, OPEN_FILE_MODES.get("read")) as file:
            data = file.read()
            keys_list = data.split(DIVIDER_IN_FILES)
            self.container.update(keys_list)
