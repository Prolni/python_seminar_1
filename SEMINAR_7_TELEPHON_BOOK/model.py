def get_contact():
    name = input('ВВЕДИТЕ ИМЯ: ')
    phone = input('ВВЕДИТЕ НОМЕР ТЕЛЕФОНА: ')
    return f'{name} || {phone} \n'
    
def find_contact(book, req):
    a = ''
    for i in book:
        if i.find(req) != -1:
            a = i
        if a == '':
            return "НЕТ"
        else:
            return a

def get_reques():
    return input("ПОИСК КОНТАКТА: ")

def choose_mode():
    return int(input("РЕЖИМ ЗАПИСИ - 1 ; РЕЖИМ ПОИСКА - 2; "))