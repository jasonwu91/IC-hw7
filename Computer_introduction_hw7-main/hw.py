class Judge:
    def __init__(self, answer: str) -> None:
        self.answer = int(answer)

    def guess(self, num: str) -> bool:
        print("Your guess is", num)
        
        a, b = 0
        
        for i in range(0, len(num)):
            for j in range(0, len(answer)):
                if num[i] == answer[j]:
                    if i == j:
                        a+=1
                    else:
                        b+=1
                else:
                    pass
        
        print("Your guess is " + num + "; the result is " + str(a) + "A" + str(b) + "B")
        
        if a == len(num):
            return True
        else:
            return False

def read_input(guess_len: int) -> str:
    print("Enter your guess:") 
    valid = False

    while(not valid):   
        entered = input()
        valid = True

        if (len(entered) != guess_len):
            valid = False

        for i in range(len(entered)):
            for j in range(i+1, len(entered)):
                if (entered[i] == entered[j]):
                    valid = False

        for k in entered:
            if ord(k)>57 or ord(k)<48:
                valid = False

        if not valid:
            print("Invalid, please enter your guess again:")

    return entered
    


def enter_answer() -> str:
    return input()
