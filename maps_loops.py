def find_max_value(dict):
    a=""
    max= 0
    for key,value in dict.items():
        if value > max:
            max = value
            a = key
    return a
print(find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}))


def reverse_dict(dic):
    newdic= dict()
    for key, value in dic.items():
        if value in newdic:
            newdic[value]+=key
        else:
            newdic[value]=key
    return newdic
print(reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2}))


def word_freq_counter(words):
    dic=dict()
    for word in words:
        if word not in dic:
            dic[word]=1
        else:
            dic[word]+=1
    return dic

print(word_freq_counter(["apple", "banana", "apple", "orange", "banana", "apple"]))


def find_biggest_expense(expenses):
    highest_avg_expense = ""
    highest_avg = 0

    for expense in expenses:
        total = 0
        count = 0
        for cost in expenses[expense]:
            total += cost
            count += 1
        average = total / count

        if average > highest_avg:
            highest_avg = average
            highest_avg_expense = expense

    return highest_avg_expense

print(find_biggest_expense({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}))


def sum_of_expenses(expenses):
    sum_expenses = {}
    for expense in expenses:
        total = 0
        for cost in expenses[expense]:
            total += cost
        sum_expenses[expense] = total
    return sum_expenses


def sum_of_expenses_by_type(expenses):
    sum_by_type = {}
    for expense in expenses:
        for item in expenses[expense]:
            expense_type = item[0]
            cost = item[1]
            if expense_type not in sum_by_type:
                sum_by_type[expense_type] = 0
            sum_by_type[expense_type] += cost
    return sum_by_type
