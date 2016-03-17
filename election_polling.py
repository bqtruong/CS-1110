import csv
def read_data_file(filename):
    with open(filename) as file:
        fileread = csv.reader(file)
        returnfile = [row for row in fileread]
    for row in range(len(returnfile)):
        for char in range(len(returnfile[0])):
            if returnfile[row][char].isnumeric():
                returnfile[row][char] = int(returnfile[row][char])
    return returnfile       
def poll_winner(poll_to_examine):
    values = poll_to_examine[4:8]
    candidates = ["Cruz", "Kasich", "Rubio", "Trump"]
    margin = max(values)
    second = 0
    for x in values:
        if x > second and x != margin:
            second = x
    margin = "+" + str(margin - second)
    winner = [candidates[values.index(max(values))], margin]
    return winner
def latest_poll_winner_by_state(state):
    states = ["FLORIDA", "OHIO", "NC"]
    filenames = ["florida-gop.csv", "ohio-gop.csv", "nc-gop.csv"]
    return poll_winner(read_data_file(filenames[states.index(state)])[0])
def average_of_polls(state, number_of_polls=5):
    states = ["FLORIDA", "OHIO", "NC"]
    filenames = ["florida-gop.csv", "ohio-gop.csv", "nc-gop.csv"]
    breakset = read_data_file(filenames[states.index(state)])[0:number_of_polls]
    average = ["Average Poll", number_of_polls, -1, -1, -1, -1, -1, -1]
    sums = [0, 0, -1, -1, -1, -1, -1, -1] #0 is placeholder value for loop convenience
    for row in breakset:
        for x in range(2,8):
            sums[x] += row[x]
    sums = [int(sums[x]/number_of_polls) for x in range(2,8)]
    average[2:8] = sums
    return average
