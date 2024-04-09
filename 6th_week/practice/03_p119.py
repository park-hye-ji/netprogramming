days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30,'December':31}

month=input()

day=days.get(month)
print(day)

print(sorted(days))

for i in days:
    day=days.get(i)
    if day==31:
        print(i)

print(sorted(days.items(), key=lambda t: t[1]))

word_3=input("input month for 3 word: ")
for i in days:
    day=days.get(i)
    if word_3 in i:
        print(i)
