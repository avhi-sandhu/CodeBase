from os import stat


def promptmsg():
    print('''There are a total of 50 states \nin the great country of USA.\n''')

    print("Name all of them in the shortest time to win!!!")
    return


def plist(sl):
    for i in range(len(sl)):
        print(sl[i])
    return


def main():
    print("-------------------------------")
    print("Welcome to the US State Guess")
    print("-------------------------------")
    promptmsg()

    stateNum = 1
    c_guesses = []
    statelist = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
                 'Montana',
                 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
                 'Wisconsin', 'Wyoming']

    while stateNum < len(statelist) + 1:

        usrinp = input("Please enter a state: ")

        if stateNum == len(statelist) + 1:
            print("Yay!!! All states guessed, Good Job")
            return

        elif (usrinp in statelist) and (usrinp not in c_guesses):
            print("Correct! {} more to go....\n".format(
                len(statelist) - stateNum))
            c_guesses.append(usrinp)
            stateNum += 1
            # plist(c_guesses)

        elif (usrinp in statelist) and (usrinp in c_guesses):
            print("Input already guessed...")

        elif usrinp.lower() == 'end':
            print("You guessed {} states correctly. Goodbye!".format(stateNum - 1))
            # plist(c_guesses)
            return

        elif usrinp.lower() == 'list':
            iterv = 1
            for state in c_guesses:
                print(str(iterv) + '.' + state + '\n')
                iterv += 1

        else:
            print("Incorrect....")

    return


main()
