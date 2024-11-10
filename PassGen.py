import secrets
import string

class PassGen:
    def __init__(self, digits, letters, punct, length):
        """Constructors for variables within the class"""
        self.digits = digits
        self.letters = letters
        self.punct = punct
        self.length = length

        # choose characters (at least 2 sets required)
        if self.digits == 'y' and self.letters == 'y' and self.punct == 'y':
            self.possible_characters = string.digits + string.ascii_letters + string.punctuation
        elif self.digits == 'n' and self.letters == 'y' and self.punct == 'y':
            self.possible_characters = string.ascii_letters + string.punctuation
        elif self.digits == 'y' and self.letters == 'n' and self.punct == 'y':
            self.possible_characters = string.digits + string.punctuation
        elif self.digits == 'y' and self.letters == 'y' and self.punct == 'n':
            self.possible_characters = string.digits + string.ascii_letters


    def generate_password(self):
        password = ''.join(secrets.choice(self.possible_characters) for i in range(self.length))

        return password
