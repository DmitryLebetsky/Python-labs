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
                return []
            else:
                return []
