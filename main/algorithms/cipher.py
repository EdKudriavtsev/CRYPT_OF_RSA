class Cipher:
    @staticmethod
    def count_power_module(a, b, m):
        result = 1
        for num in range(b):
            result *= a
            result %= m
        return result

    @staticmethod
    def encrypt(data: str, public_key: int, module_num: int):
        result = []
        for letter in data:
            encrypted_letter = Cipher.count_power_module(ord(letter), public_key, module_num)
            result.append(str(encrypted_letter))
        return ' '.join(result)

    @staticmethod
    def decrypt(data: str, private_key: int, module_num: int):
        data = data.split()
        result = []
        for num in data:
            decrypted_letter = '[UNDEFINED]'
            if num.isdigit():
                try:
                    decrypted_letter = chr(Cipher.count_power_module(int(num), private_key, module_num))
                except ValueError:
                    pass
            result.append(str(decrypted_letter))
        return ''.join(result)


encrypted_str = Cipher.encrypt('abcd', 422113, 1270807)
print(encrypted_str)
print(Cipher.decrypt(encrypted_str, 606193, 1270807))
