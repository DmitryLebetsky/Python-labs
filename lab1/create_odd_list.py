from constants import STOP_VALUE


def create_odd_list():
    should_stop = False
    full_list = []
    odd_list = []

    while not should_stop:
        entered_number = input("Next element: ")
        if entered_number == STOP_VALUE:
            should_stop = True
            continue
        try:
            entered_number = int(entered_number)
            full_list.append(entered_number)
        except ValueError:
            print("This is not integer! Try again :)")

    print("List was created: " + str(full_list))

    for number in full_list:
        if number % 2 == 1:
            odd_list.append(number)
    return odd_list

