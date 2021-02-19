from string import ascii_uppercase as alphabet

class Hangman:   
    def __init__(self, word):
        self.word = word.upper()
        self.wlist = ["-" for i in range(len(word))]
        self.tried = []
        self.life = 9

    def get_indexes(self, char):
        return [k for k, v in enumerate(self.word) if char==v]

    def assert_rules(self, choice):
        if len(choice) > 1:
            print("<Hangman> You can only choose one character!")
            return False

        elif choice not in alphabet:
            print("<Hangman> The character must be a letter!")
            return False
        
        elif choice in self.tried:
            print("<Hangman> You already tried with this character!")
            return False

        return True

    def update_screen(self):                               
        life_bar = "Life [" + "■" * self.life + " " * (9-self.life) + "]"
        print(life_bar)
        print("Already choosen:", ", ".join(self.tried))
        print(self.wlist)
      

    def play(self):
        while True:
            
            if not self.life:
                break
            
            self.update_screen()
            choice = input("\n<Hangman> Choose a letter: ").upper()
            
            while not self.assert_rules(choice):
                choice = input("\n<Hangman> Choose a letter: ").upper()

            if choice in self.word:
                indexes = self.get_indexes(choice)
                for index in indexes:
                    self.wlist[index] = choice
            else:
                self.life -= 1
            self.tried.append(choice)

            if not "-" in self.wlist:
                print("<Hangman> You won. Congratulations!")
                return

            print("-" * 70)
            
        self.update_screen()                    
        print("<Hangman> You lost!")


if __name__ == "__main__":
    game = Hangman("SOMETHING")
    game.play()
