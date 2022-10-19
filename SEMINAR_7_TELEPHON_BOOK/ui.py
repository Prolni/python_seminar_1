import model
import logger




while True:
    mode = model.choose_mode()
    if mode == 1:
        logger.write_new(model.get_contact())
    elif mode == 2:
        contact = model.get_reques()
        book = logger.get_book()
        print(model.find_contact(book, contact))
    elif mode == 0:
        print('выход')
        break
    else:
        print('такого режима нет')