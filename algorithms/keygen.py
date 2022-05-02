from random import randint
from .math_functions import find_mod_inverse, binary_search
from .prime_numbers import get_prime_nums


class KeyGen:
    MAX_COUNT = 10000

    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.F = 0
        self.e = 0
        self.d = -2
        self.prime_numbers = get_prime_nums()

    def generate_prime(self):
        self.p = self.prime_numbers[randint(0, len(self.prime_numbers) - 1)]
        self.q = self.prime_numbers[randint(0, len(self.prime_numbers) - 1)]
        while self.q == self.p:
            self.q = self.prime_numbers[randint(0, len(self.prime_numbers) - 1)]

    def calculate_module(self):
        self.n = self.p * self.q
        self.F = (self.p - 1) * (self.q - 1)

    def calculate_public(self):
        L = binary_search(self.prime_numbers, self.F)
        self.e = self.prime_numbers[L - randint(1, L // 2)]

    def calculate_private(self):
        count = 0
        while self.d < 0 and count < KeyGen.MAX_COUNT:
            self.d = find_mod_inverse(self.e, self.F)[1]
            count += 1
        if count == KeyGen.MAX_COUNT:
            return False
        else:
            return True

    def main_generate(self):
        while True:
            self.generate_prime()
            self.calculate_module()
            self.calculate_public()
            if self.calculate_private():
                return [self.e, self.d, self.n]
