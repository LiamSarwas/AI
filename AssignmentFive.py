def main():
    senators = read_data()
    percent_correct(senators)


def read_data():
    senators = []
    with open('/Users/Liam/Desktop/Homework/UAA/test-house-votes-1984.txt', 'r') as file:
        for line in file:
            row = line.strip().split(" ")
            if row[0] != 'y' and row[0] != 'n':
                continue
            senators.append(row)
    return senators


def percent_correct(senators):
    incorrect = 0
    for i in range(0, len(senators)):
        party = ''
        if senators[i][3] == "n":
            party = "democrat"
        elif senators[i][3] == "y":
            if senators[i][2] == "y":
                if senators[i][6] == "n":
                    party = "democrat"
                elif senators[i][6] == "y":
                    party = "republican"
            elif senators[i][2] == "n":
                party = "republican"

        if party != senators[i][16]:
            print(senators[i])
            incorrect += 1

    print('This incorrectly categorized: ', incorrect/100, ' percent of the representatives.')


main()
