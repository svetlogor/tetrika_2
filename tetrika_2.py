
def file_read(path):
    """
    Чтение файла.
    :param path: Путь и название
    :return: Текст
    """
    with open(path, 'r') as f:
        file = f.read()
    return file

def file_split_ip(text):
    """
    Вытаскивает ip адреса.
    :param text: Текст
    :return: Список ip адресов (list)
    """
    text1 = text.split('\n')
    split_ip = []
    sum_ip = 0
    for i in text1:
        if i != '':
            ip = i.split('\t')[1]
            sum_ip += 1
            split_ip.append(ip)
    return split_ip

def top_5_ip(list_ip):
    """
    Выводит 5 часто встречающихся ip адресов.
    :param list_ip: Список ip адресов (list)
    :return: Список (list)
    """
    dict_ip = {}
    top_5_list_ip = []
    # Произведение повторяющихся ip адресов
    # Составляет словарь {'ip адрес' : произведение}.
    # Пример {'72.110.191.15': 426, '142.93.168.247': 372, ... }
    for ip in list_ip:
        if ip in dict_ip:
            value = dict_ip[ip]
            dict_ip.update({ip: value + 1})
        else:
            dict_ip.update({ip: 1})
    # Сортировка по убыванию
    sorted_ip = sorted(dict_ip.values(), reverse=True)
    # Поиск ТОП 5 адресов
    for i in sorted_ip[:5]:
        for key, value in dict_ip.items():
            if i == value:
                if key not in top_5_list_ip:
                    top_5_list_ip.append(key)
    return top_5_list_ip


if __name__ == '__main__':
    # Путь и название
    path = 'hits.txt'
    print('ТОП 5 ip адресов:', top_5_ip(file_split_ip(file_read(path))))
