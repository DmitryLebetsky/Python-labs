from contants import EXISTING_USERS_PATH, OPEN_FILE_MODES, DIVIDER_IN_FILES


class User:
    def __init__(self, name):
        self.name = name
        self.container = self.check_container_existing()

    def check_container_existing(self):
        with open(EXISTING_USERS_PATH, OPEN_FILE_MODES.get("read")) as file:
            data = file.read()
            users_list = data.split(DIVIDER_IN_FILES)

            if self.name in users_list:
                #  create container according to user's data in database
                return set()
            else:
                return set()

    def add(self, keys_list):
        self.container.update(keys_list)

    def remove(self, key):
        self.container.discard(key)

    def find(self, keys_list):
        found_keys = [key for key in keys_list if key in self.container]
        return found_keys

    def list(self):
        return self.container

