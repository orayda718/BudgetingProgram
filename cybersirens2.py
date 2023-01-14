# Cyber-Sirens' Budgeting App
# Team members: Vaishnavi, Orayda, Shriya, Isabella

print("Hi, Welcome to the Cyber Sirens Budgeting app!\n")

# creating the categories
categories = []
cat1 = input("Please enter a category or type 'x' to finish: ")
while cat1.upper() != "X":
    categories.append([cat1])
    cat1 = input("Please enter a category or type 'x' to finish: ")
# print(categories)

print("\n")

# the budgets for each category
budgets = []
for i in categories:
    budget = int(input("Please set a budget for " + i[0] + " : "))
    budgets.append(budget)
# print(budgets)

totSpend = 0

print("\n")

for x in categories:
    p = int(input("Please input a purchase amount for " + str(x[0]) + " or enter '-1' to stop: "))

    if p != -1:
        x.append([p])
        totSpend += p

    # print(categories)

    for y in x:
        while p != -1:
            p = int(input("Please input another purchase amount for " + str(x[0]) + " or enter '-1': "))
            if p != -1:
                x[1].append(p)
                totSpend += p

            # print(categories)

    print("\n")

print("Total Spending = " + str(totSpend))  # total expenditure

print("\n")

num = 0
for x in categories:
    sum = 0
    purchases = x[1]
    for i in purchases:
        sum += i

    print(str(x[0]) + " spending = " + str(sum))  # total expenditure for each category

    if sum > budgets[num]:
        print(str(x[0]) + " spending was over budget by " + str(sum - budgets[num]))
    elif sum < budgets[num]:
        print(str(x[0]) + " spending budget was under by " + str(budgets[num] - sum))
    else:
        print("The budget has been spent")

    num += 1
    print("\n")
