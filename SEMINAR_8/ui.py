from logger import write_new_data as wnd
from logger import read_data as rd
from logger import alter as alt
from model import add_new_data as addnd
from model import data_search as ds
from model import selection_mode as sm
from model import editing_data as ed

while True:
    mode = sm()
    if mode == 1: 
        wnd(addnd())
    
    elif mode == 2: 
        print(ds(rd()))

    elif mode == 3: 
        print(rd())

    elif mode == 4: 
        old_str = ds(rd())
        print(old_str)
        while old_str.count('\n') > 0:
            print('Уточните критерии поиска, чтобы получить запись конкретного сотрудника')
            old_str = ds(old_str)
            print(old_str)
        new_str = ed(old_str)
        alt('seminar8_data.txt', old_str, new_str)

    elif mode == 0: 
        print('Работа закончена')
        break
    
    else:
        print(f'Режим {mode} находится в разработке')