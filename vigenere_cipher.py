import numpy as np

class VigenerCipher:
    ''' a class that encrypts and decrypts messages using the Vigener Cipher method'''
    def __init__(self):
        
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = np.arange(0,26)
        
        
        self._alpha_toint = dict(zip(alphabet,numbers))
        self._int_toalpha = dict(zip(numbers, alphabet))
        
        
        # key length, eq, longer, shorter is ideal
        # remove all non-alphanumerics and store their indices to replace later
    
    
    
    def encrypt(self, key, message):
        # creates an encryption using the generate key and stripped message
        # returns an encryption with all the numbers and characters. 
        # case sensitive
        msg_list = list(enumerate(message))
        _numbers = {i:no for i,no in msg_list if not no.isalpha()}
        _messo = [no for no in message if no.isalpha()]
        _caps = [i for i in range(len(_messo)) if _messo[i].isupper()]
        _messo = [no.lower() for no in message if no.isalpha()]
        
        
        def generate_key( key):
            if key.isalpha():
                key = key.lower()
                key = list(key)
                if len(_messo) < len(key):
                    key = key[:len(string)]
            
                _cipher_key = [key[i%len(key)] for i in range(len(_messo)) ]
                return _cipher_key
        
        
            else:
                raise Exception('Key must contain alphabetic characters only')
        _cipher = generate_key(key)
        message2numbers = [self._alpha_toint[i] for i in _messo]
        cipher2numbers = [self._alpha_toint[i] for i in _cipher]
        
        encrypted_number = (np.array(message2numbers) + np.array(cipher2numbers)) % 26
        encrypted_text = [self._int_toalpha[i] for i in encrypted_number]
        
        for i in _caps:
            encrypted_text[i] = encrypted_text[i].upper()
        for i,j in _numbers.items():
            encrypted_text.insert(i,j)
    
        return ''.join(encrypted_text)
    
    
    def decrypt(self, key, message):
        # decrypt the message using
        
        msg_list = list(enumerate(message))
        _numbers = {i:no for i,no in msg_list if not no.isalpha()}
        _messo = [no for no in message if no.isalpha()]
        _caps = [i for i in range(len(_messo)) if _messo[i].isupper()]
        _messo = [no.lower() for no in message if no.isalpha()]
        
        
        def generate_key( key):
            if key.isalpha():
                key = list(key)
                if len(_messo) < len(key):
                    key = key[:len(string)]
            
                _cipher_key = [key[i%len(key)] for i in range(len(_messo)) ]
                return _cipher_key
        
        
            else:
                raise Exception('Key must contain alphabetic characters only')
        _cipher = generate_key(key)
        message2numbers = [self._alpha_toint[i] for i in _messo]
        cipher2numbers = [self._alpha_toint[i] for i in _cipher]
        
        decrypted_number = ((np.array(message2numbers) - np.array(cipher2numbers)) + 26) % 26
        decrypted_text = [self._int_toalpha[i] for i in decrypted_number]
        
        for i in _caps:
            decrypted_text[i] = decrypted_text[i].upper()
        for i,j in _numbers.items():
            decrypted_text.insert(i,j)
    
        return ''.join(decrypted_text)
    
    
def main():
    message2encrypt = input('Please enter message you wish to encode: \n')
    encryption_key = input("Please enter an encryption key. Must be alphabetic characters only: \n")
    
    obj = VigenerCipher()
    print('''\n\n\n  Your encrypted message is : \n{}\n\n\n
    '''.format(obj.encrypt(key = encryption_key, message = message2encrypt))) 
          
    
    message2decrypt = input('Please enter message you wish to decode: \n')
    decryption_key = input("please enter the encryption key. Must be alphabetic characters only: \n")
    
    obj2 = VigenerCipher()
    print('''\n\n\nYour decrypted message is : \n{}\n\n\n
    '''.format(obj2.decrypt(key = decryption_key, message = message2decrypt)) )
    
    
    
if __name__ == '__main__':
    main()