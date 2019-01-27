def func_string_template(data_attrs):
    align_sign = {
        'LEFT': '',
        'RIGHT': '>',
        'MID': '^',
    }
    def wrapper(real_data):
        return "{:{padding}{align}{len}}".format(
            real_data,
            padding=data_attrs['PADDING'],
            align=align_sign.get(data_attrs['ALIGN']),
            len=data_attrs['LEN'])
    return wrapper


if __name__ == '__main__':
    data_dict = {
        'ID': 'ABC',
        'NICK': 'DUCK',
    }

    func_ID = func_string_template(
        {'LEN': 13, 'ALIGN': 'LEFT', 'PADDING': ''})
    func_NICK = func_string_template(
        {'LEN': 20, 'ALIGN': 'MID', 'PADDING': '*'})
    layout = [func_ID(data_dict.get('ID')),
        func_NICK(data_dict.get('NICK'))]

    result = list()
    for item in layout:
        result.append(f'{item}')
    print(''.join(result))
