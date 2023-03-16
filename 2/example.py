#give_me_money
account = 1000
limit_for_loan = 500
limit_for_withdraw = 400
def give_me_money(amount):
    if amount <= account:
        if amount > limit_for_withdraw:
            a = amount//limit_for_withdraw
            b = amount%limit_for_withdraw
            for i in range(a):
                print(limit_for_withdraw)
            print(b)
        else:
            print(amount)
    elif amount <= (account + limit_for_loan):
        a = amount//limit_for_withdraw
        b = amount%limit_for_withdraw
        for i in range(a):
            print(limit_for_withdraw)
        print(b)
    else:
        c = amount - (account + limit_for_loan)
        print(f'''you don't have enough money, you have to deposite {c} dollars''')

# give_me_money(500)
# give_me_money(1000)
# give_me_money(1500)

#미니실습1
def question():
    animal = input()
    if animal == '고양이':
        print('야옹')
    else: 
        print(f'''안녕 난 {animal}이 아니라 알락꼬리꼬마도요야.''')
#question()

#미니실습2
count = 10
while count >= 1:
    print('발사')
    print(count)
    count -= 1