from random import randint

money=50
while(money>0 and money <100):
    coin = randint(1,2)
    answer = randint(1,2)
    if (answer==coin):
        money=money+9
    else:
        money=money-10

    print(money)