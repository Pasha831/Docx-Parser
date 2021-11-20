
import docx  # библиотека для работы с Word

doc = docx.Document("law.docx")  # считываем весь документ
all_paras = doc.paragraphs  # расчленяем текст на параграфы


all_paras = [x for x in all_paras if len(x.text) != 0]  # избавляемся от пустых строк

number = int(input())  # просим пользователя ввести номер абзаца
print(all_paras[number - 1].text)  # выводим интересующий его абзац

