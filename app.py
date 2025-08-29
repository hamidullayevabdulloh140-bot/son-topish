class GuessingGame:
    def __init__(self):
        import random
        self.number = random.randint(1, 100)
        self.is_solved = False
    
    def guess(self, number):
        if number > self.number:
            print("Siz kiritgan son katta")
        elif number < self.number:
            print("Siz kiritgan son kichik")
        else:
            print("To'g'ri javob!")
            self.is_solved = True

game = GuessingGame()

while not game.is_solved:
    user_input = input("Son kiriting (1-100): ")
    if user_input.isdigit():
        taxmin = int(user_input)
        game.guess(taxmin)
    else:
        print("Iltimos, faqat butun son kiriting.")



