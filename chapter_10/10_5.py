# 10-5. Programming Poll: Write a while loop that asks people why they
# like programming. Each time someone enters a reason, add their reason
# to a file that stores all the responses.

filename = 'programming_poll.txt'

answers = []
while True:
    answer = input('Why do you like programming?\n(enter "q" to quit): ')
    answers.append(answer)
    if answer == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(answer + '\n')
