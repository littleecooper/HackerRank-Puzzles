'''
5 - total students
Harry - name of first student
37.21 - score of first student
Berry - so on
39.56 - so on
Tina
37.2
Akriti
41
Harsh
39
'''




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




