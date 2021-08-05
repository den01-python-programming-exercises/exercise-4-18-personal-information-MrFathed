from personal_information import PersonalInformation

def main():
    #write your code below this line
    people = []

    while True:
        first_name = input("First name:")

        if not first_name:
            break

        last_name  = input("Last name:")
        id_num = input("Identification number:")
        people.append(PersonalInformation(first_name, last_name, id_num))

    for person in people:
        print(person.get_first_name(), person.get_last_name())

if __name__ == '__main__':
    main()
