d = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

print("전화번호가 8로 끝나는 사용자 이름: ")
for person in d:
    if person['phone'].endswith('8'):
        print(person['name'])

print("이메일이 없는 사용자: ")
for person in d:
    if not person['email']:
        print(person['name'])

def find_user(name):
    for person in d:
        if person['name'] == name:
            return person['phone'], person['email']
    return False

who = input("사용자 이름을 입력하세요: ")
user = find_user(who)

if user:
    print(f"전화번호: {user[0]}, 이메일: {user[1]}")
else:
    print("이름이 없습니다.")
