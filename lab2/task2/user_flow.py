from contants import EXISTING_USERS_PATH, OPEN_FILE_MODES, DIVIDER_IN_FILES, MULTIPLE_KEYS_COMMANDS, ONE_KEY_COMMANDS,\
    NO_KEY_COMMANDS
from user import User


class UserFlow:
    def __init__(self):
        users_list = self.get_users_list()
        self.users_containers = dict()
        for user in users_list:
            self.users_containers[user] = User(user)

        username = input("Enter username: ")
        self.current_user = User(username)

        self.start_interactive_mode()

    def start_interactive_mode(self):
        should_quit = False

        print("List of commands:")
        print("-add <key1> <key2> ...")
        print("-remove <key>")
        print("-find <key1> <key2> ...")
        print("-show")
        print("-grep <regexp>")
        print("-save")
        print("-load <username>")
        print("-switch <username>")
        print("-quit")

        while not should_quit:
            input_string = input("Input command: ")
            if input_string == "":
                print("Incorrect input!")
                continue
            input_list = input_string.split(" ")
            command = input_list[0]

            if command in MULTIPLE_KEYS_COMMANDS:
                keys = input_list[1:]
                should_continue = not self.check_keys(keys)
                if should_continue:
                    continue
                else:
                    if command == "add":
                        self.current_user.add(keys)
                    elif command == "find":
                        print(self.current_user.find(keys))

            elif command in ONE_KEY_COMMANDS:
                keys = input_list[1:]
                should_continue = not self.check_keys(keys, True)
                if should_continue:
                    continue
                if command == "remove":
                    self.current_user.remove(keys[0])
                elif command == "grep":
                    print(self.current_user.grep(keys[0]))
                elif command == "load":
                    is_user_exist = self.check_user_exist(keys[0])
                    if not is_user_exist:
                        continue
                    else:
                        self.current_user.load(keys[0])
                elif command == "switch":
                    is_user_exist = self.check_user_exist(keys[0])
                    if not is_user_exist:
                        continue
                    else:
                        self.propose_to_save()
                        self.current_user = self.users_containers[keys[0]]

            elif command in NO_KEY_COMMANDS:
                if len(input_list) != 1:
                    print("This command doesn't have arguments!")
                    continue
                if command == "show":
                    print(self.current_user.list())
                elif command == "save":
                    self.current_user.save()
                    self.users_containers[self.current_user.name] = self.current_user.container

            elif command == "quit":
                self.propose_to_save()
                should_quit = True

            else:
                print("Incorrect command!")
                continue

    def propose_to_save(self):
        should_save = input("Enter 'yes' if you want to save container: ")
        if should_save == "yes":
            self.current_user.save()
            self.users_containers[self.current_user.name] = self.current_user

    def check_user_exist(self, user):
        if user not in self.users_containers:
            print("No such user in database :(")
            return False
        return True

    def check_keys(self, keys, one_key_only=False):
        if one_key_only:
            if len(keys) != 1:
                print("This command must has only one argument!")
                return False
        if len(keys) == 0:
            print("This command need arguments!")
            return False
        for key in keys:
            if key == "":
                print("Argument can not be an empty string")
                return False
        return True

    def get_users_list(self):
        with open(EXISTING_USERS_PATH, OPEN_FILE_MODES.get("read")) as file:
            data = file.read()
            users_list = data.split(DIVIDER_IN_FILES)
            return users_list
