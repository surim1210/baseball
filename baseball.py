from random import randint

ranums = []
guess = []
count = 0
strike = 0
check = 0

# 랜덤 숫자 뽑기
while len(ranums) < 3:
    new_nums = randint(0, 9)
    while new_nums in ranums: # 중복 숫자 확인
        new_nums = randint(0, 9)
    ranums.append(new_nums)
print(ranums)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

# 사용자 숫자 뽑기
def user_input():
     tries = 1
     count = 0
     while len(guess) < 3:
         print("세 수를 차례대로 입력하세요.")
         count += 1
         while tries <= 3:
            guess_num = int(input(("%d번째 수를 입력하세요: " % (tries))))
            if guess_num >= 10: # 범위 확인
                print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
                continue
            elif guess_num in guess: # 중복 체크
                print("중복되는 수 입니다. 다시 입력해주세요.")
                continue
            else:
                guess.append(guess_num)
            tries += 1

# strike & ball 확인
while strike < 3:
    strike = 0
    ball = 0
    user_input()
    while check < 3:
        if guess[check] == ranums[check]:
            strike += 1
        elif guess[check] in ranums:
            ball += 1
        check += 1
    print("%dS %dB\n" %(strike, ball))
    check = 0
    if strike == 3:
        print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다."%(count))
    else:
        guess.clear() # 사용자 입력 초기화