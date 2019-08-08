"""
주어진 format에 맞춰 문자열을 생성하는 함수를 생성
"""


def xstring_maker(length=0, align='LEFT', padding=''):
    """
    param으로 받은 length, align, padding으로 문자열 format을 설정
    """
    ALIGN_SIGN = {
        'LEFT': '',
        'RIGHT': '>',
        'MID': '^',
    }

    def wrapper(data):
        return "{:{padding}{align}{len}}".format(
            data[:length],
            padding=padding,
            align=ALIGN_SIGN.get(align),
            len=length)
    return wrapper


if __name__ == '__main__':
    data_sample = {
        'NAME': 'ABC',
        'NICK': 'DUCK',
    }

    name = string_maker(length=13)
    nick = string_maker(length=20, align='MID', padding='*')
    layout = [name(data_sample.get('NAME')), nick(data_sample.get('NICK'))]

    print(''.join([f'{item}' for item in layout]))
