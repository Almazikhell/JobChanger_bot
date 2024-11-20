from telebot import types

all_tags = ["Программист", "Дизайнер", "Художник", "Музыкант", "Репетитор", "Сценарист"]

def generate_markup(page=0,pages=[]):
    kb = types.InlineKeyboardMarkup()

    if page < 0:
        page = 0
    print(pages)
    kb.row(types.InlineKeyboardButton(text = "<<",callback_data=f"page_{page - 1 if page - 1 >= 0 else -1}"),
           types.InlineKeyboardButton(text=">>", callback_data=f"page_{page + 1 if len(pages)-1 >= page +1 else -1}"))
    return kb

def generate_tags():
    kb = types.InlineKeyboardMarkup()
    for i, el in enumerate(all_tags):
        kb.add(types.InlineKeyboardButton(text=el,callback_data=f"tag_{i}"))
    kb.add(types.InlineKeyboardButton(text="!!Другое!!", callback_data="other_tag"))
    return kb
