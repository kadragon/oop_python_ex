"""
Title       시저 암호
Reference   나만의 Python Game 만들기 Chapter 14 p.297
Author      kadragon
Date        2018.09.07
"""

# 시저 암호의 설정값의 최대치를 결정함. 알파벳 'a'~'z'가 26개 이기 때문에 26으로 설정
MAX_KEY_SIZE = 26


def get_mode():
    """
    사용자로 부터 암호화를 할 것인지, 복호화를 할 것인지 물어보는 메소드 Ver.1
    :return: encrypt OR e OR decrypt OR d
    """
    while True:
        in_mode = input('Do you wish to encrypt or decrypt a message?').lower()
        # if in_mode in ['encrypt', 'e', 'decrypt', 'd'.split():
        if in_mode in 'encrypt e decrypt d'.split():
            return in_mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def get_mode_other():
    """
    사용자로 부터 암호화를 할 것인지, 복호화를 할 것인지 물어보는 메소드 Ver.2
    :return: encrypt OR e OR decrypt OR d
    """
    while True:
        in_mode = input('Do you wish to encrypt or decrypt a message?').lower()
        if in_mode.startswith('e'):
            return 'encrypt'
        elif in_mode.startswith('d'):
            return 'decrypt'
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def get_message():
    """
    암호화나 복호화 할 문자열을 입력 받는 메소드
    :return: 사용자가 입력한 문자열을 반환함.
    """
    return input('Enter your message: ')


def get_key():
    """
    암호화 키를 입력 받아, 1 <= a <= MAX_KEY_SIZE 을 만족하면 입력 받은 값을 반환하고 아니면, 다시 입력 받는 함수
    :return: 1 <= a <= MAX_KEY_SIZE 를 만족하는 정수 a
    """
    while True:
        """
        사용자로 부터 암호화 키를 입력 받는데, 사용자가 정수가 아닌 값을 넣어서
        int() 과정에 ValueError 가 발생할 경우 예외처리
        """
        try:
            user_in_key = int(input('Enter the key number (1~%d)' % MAX_KEY_SIZE))
        except ValueError:
            print("Input Value Error!")
            continue

        # MAX_KEY_SIZE 와 값을 비교한다. python 은 이게 된다!
        if 1 <= user_in_key <= MAX_KEY_SIZE:
            return user_in_key
        else:
            print("Ranges Error!")


def get_trans_message(mode, message, key):
    """
    mode 를 확인하여, message를 key 기준으로 암호화 or 복호화하여 반환함
    :param mode: encrypt OR e OR decrypt OR d
    :param message: 사용자가 입력한 값
    :param key: 암호화 키 (이동 횟수)
    :return: mode에 의해 암호화 or 복호화된 값
    """
    # mode 의 상태를 확인하여 key 값을 더할지, 뺄지를 결정한다.
    if mode[0] == 'd':
        key = -key

    translated = ''  # 반환할 문자열 생성

    for symbol in message:
        if symbol.isalpha():  # isalpha() 알파벳인지 확인해주는 메소드
            """
            ord(chr) 
            Return the Unicode code point for a one-character string. 
            """
            num = ord(symbol)
            num += key

            if symbol.isupper():  # isupper() 대문자인지 확인해주는 메소드
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():  # islower() 소문자인지 확인해주는 메소드
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            """
            chr(int)
            Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
            """
            translated += chr(num)
        else:
            translated += symbol

    return translated


mode = get_mode()  # 암호화인지 복호화인지 모드를 입력 받는다.
message = get_message()  # 진행할 메시지를 입력 받는다.
key = get_key()  # 암호화 키를 입력 받는다.

print('Your translated text is: ')
print(get_trans_message(mode, message, key))
