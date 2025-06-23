import os

def path(note_name):
    return f'/home/lomalo890/Desktop/Eduson/workbooks/python/projects/note/{note_name}.txt'
def build_note(note_name, note_text):
    if note_name[0].isdigit():
        raise "Нельзя, чтобы файл начинался с цифры"
    with open(path(note_name), 'w') as file:
        file.write(note_text)
def create_note(note_name, note_text):
    try:
        build_note(note_name, note_text)
    except Exception as e:
        print(e)
def read_note(note_name):
    try:
        with open(path(note_name), 'r') as file:
            print(file.read())
    except FileNotFoundError as error:
        print(error)
def delete_note(note_name):
    if os.path.isfile(path(note_name)):
        os.remove(path(note_name))
    else:
        print('Заметка не найдена.')
def display_notes():
    files = sorted(os.listdir('/home/lomalo890/Desktop/Eduson/workbooks/python/projects/note/'), key=len)
    for file in files:
        print(file)
def display_sorted_notes():
    files = sorted(os.listdir('/home/lomalo890/Desktop/Eduson/workbooks/python/projects/note/'), key=len)[::-1]
    for file in files:
        print(file)


def main():
    commands = """
Здравствуйте!

1. Создать заметку.
2. Прочитать заметку.
3. Удалить заметку.
4. Вывести все заметки (по возростанию)
5. Вывести все заметки (по убыванию)
X. Выйти из приложения.

Нажмите соответствующую клавишу.
"""
    while True:
        print(commands)
        command = input()
        match command:
            case '1':
                note_name = input('Введите название заметки: ')
                note_text = input('Введите текст заметки: ')
                build_note(note_name, note_text)
            case '2':
                read_note(input('Введите название заметки: '))
            case '3':
                delete_note(input('Введите название заметки: '))
            case '4':
                display_notes()
            case '5':
                display_sorted_notes()
            case 'X':
                break













build_note("note1", "Я пошул гулять1")
build_note("note3", "Я пошул гулять1")
build_note("note22", "Я пошул гулять2")
build_note("note333", "Я пошул гулять3")


read_note('note3')
read_note('note1')
read_note('note2')
print()
display_notes()
display_sorted_notes()

delete_note('note1')
delete_note('note2')
delete_note('note3')
delete_note('note22')
delete_note('note333')






