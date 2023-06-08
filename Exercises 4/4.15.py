import random
lottery=random.randint(100,999)
guess=eval(input("Enter your lottery ticket number:\n"))

lotteryDigit1=lottery%10
lotteryDigit2=lottery//10
lotteryDigit3=lottery%10

guessDigit1=guess%10
guessDigit2=guess//10
guessDigit3=guess%10

print("The lottery tickect number is",lottery)

if guess==lottery:
    print("The number is exact match, You win 10,000$")
elif (guessDigit3==lotteryDigit3 and guessDigit2==lotteryDigit1 and guessDigit1==lotteryDigit2):
    print("The number Matches all digits, You win 3,000$ ")
elif (guessDigit1 == lotteryDigit1
        or guessDigit1 == lotteryDigit2
        or guessDigit1 == lotteryDigit3
        or guessDigit2 == lotteryDigit1
        or guessDigit2 == lotteryDigit2
        or guessDigit2 == lotteryDigit3
        or guessDigit3 == lotteryDigit1
        or guessDigit3 == lotteryDigit2
        or guessDigit3 == lotteryDigit3):
    print("The number matches one digit, You won 1,000$")
else:
    print("Sorry no number matches")

