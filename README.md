# HackerRank-Puzzles
I am currently using a platform called HackerRank to test my Python programming skills and wanted to showcase them on my GitHub account. 

# One of the puzzles on HackerRank focused on nested lists and the aim of the puzzle was to input data around students and their test scores and create a piece of code in Python to retrieve the two scores which were the second lowest. As there was multiple low scores, HackerRank requested that we were to pull the name of these students out of the data in an alphabetical order. Below is the code I used to acheive this. 

if __name__ == '__main__':
    name_list = []
    score_list = []
    nested_list = []
    for x in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append(([name, score]))
        score_list.append(score)
        score_list =list(set(score_list))
        score_list.sort(reverse=True)
    second_highest = score_list[-2]

    for person in nested_list:
        score = person[1]
        name = person[0]
        if score == second_highest:
            name_list.append(name)

    name_list.sort()

    for name in name_list:
        print(name)
