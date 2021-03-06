# Docx-Parser (учимся чему-то новому с Заирой =D)

### Что нам дано:
* Word файл с каким-то нормативно-правовым актом

### Что нам нужно получить:
* Разбиение файла на абзацы

---
## Подготовка:
1. Берём от Заиры docx файл с какой-то водищей:

![image](https://user-images.githubusercontent.com/46136468/142738492-279f33b3-0f1b-44d2-8880-4c41c8a38f2e.png)

2. Быстро-быстро учим python (питон, змея) и на умных щах скачиваем библиотеку для работы с файлами Word в Python:

![image](https://user-images.githubusercontent.com/46136468/142738556-5b5d03d3-dd4a-4798-adfc-72bb0cd7e8d7.png)

> **Библиотека невероятно удобная, т.к. не нужно париться и придумывать алгоритмы разбиения текста на абзацы, ведь в этой библиотеке уже есть написанные чужими руками функции, чтобы поделить текст на абзацы!**

3. Готовим чай и печеньки и идём писать код :upside_down_face:

---

## Пошла жара:

**1**. Используем библиотеку `docx` и создаём объект `doc`, который будет хранить в себе документ `law.docx`, ту самую водищу от Заиры.

![image](https://user-images.githubusercontent.com/46136468/142738737-303adb9c-e1d7-472b-925f-f4496cc80f34.png)

**2**. Библиотека `docx` имеет чрезвычайно полезный для нас метод: `doc.paragraphs`. Он позволяет нам разбить Word-файл на абзацы (параграфы) и хранить их в отдельной переменной `all_paras` (моя попытка назвать переменную осмысленно)

![image](https://user-images.githubusercontent.com/46136468/142738804-6456054f-9774-4d87-a5cb-c614037bc8dd.png)

**3**. Дальше произойдёт магия: мы заставим эту чёртову змею вывести нам абзацы (параграфы, могу и так называть), дабы мы могли ими полюбоваться:

![image](https://user-images.githubusercontent.com/46136468/142740542-500f7513-16ea-42b4-878f-396546835593.png)

Переменная `i`, которую мы изначально объявили как 1, будем нам сообщать о порядковом номере абзаца (1, 2, 3...)

Используем цикл `for` и пробежимся по всем абзацам `all_paras` с помощью переменной `para`, которая в свою очередь будет хранить содержание отдельно взятого из списка всех абзацев (текст отдельно первого абзаца, текст второго абзаца и т.д.)

Чтобы получить текст отдельного абзаца, воспользуемся методом `para.text`, который даёт нам доступ к содержанию абзаца, и выведем его вместе с порядковым номером `i` через функцию `print()`

После вывода абзаца увеличим переменную `i` на единицу, т.к. нам нужно следить за порядком и увеличивать это число.

Давай же глянем, что выводит нам эта машина:

![image](https://user-images.githubusercontent.com/46136468/142739064-a9da2873-c405-4eeb-b381-618f8fb69d72.png)

У нас есть прогресс, однако заметны и проблемы: почему абзац 2 и абзац 4, а также 6 и т.д. **пустые**?

**4**. Дело в том, что огромные отступы в виде пустой строки тоже считаются за абзац :neutral_face:

Как же решить эту проблему? Да очень просто - давай просто выкинем пустые абзацы! Следующий код нам в этом очень даже поможет:

![image](https://user-images.githubusercontent.com/46136468/142740573-aa6c22bc-1735-404b-9958-2675c4801881.png)

**Что тут мать его происходит**? Если ты не программист и совсем не знакома с Python, то это абсолютно нормальная реакция.

Обо всём по порядку. Я захотел заново объявить список всех абзацев `all_paras`, где буду хранить только не пустые абзацы. Основной ужас здесь скрывается в этом коде: `[x for x in all_paras if len(x.text) != 0]`

Скобки по краям `[...]` говорят нам, что переменная, которую мы сейчас переназначим, будет списком каких-то объектов. Например: список можно представить как набор чисел от 1 до 5: `a = [1, 2, 3, 4, 5]`. Тут числа - это значения списка `a`, к которым мы можем обраться вот так: `a[0] = 1, a[2] = 3` (*забыл сказать, все значения списка или массива начинают своё нумерование с 0!*)

Далее: `[x for x in all_paras...]` говорит нам, что мы побежим по всем абзацам, которые есть в `all_paras` (это то же самое, как мы делали в предыдущем for'е, только там за `x` выступала переменная `para`). Если бы мы не добваляли никаких условий после `...`, наш список никак бы не изменился, ведь мы бы пробежались по всем элементам и снова всех записали в тот же список.

Тут в бой вступает условие `if len(x.text) != 0`. Эта проверка позволяет нам понять, какова длинна нашего текущего абзаца `x`? Помнишь нашу цель, избавиться от пустых строк? Так вот, если длина абзаца равна нулю, т.е. он пустая строка, то мы его просто пропускаем. Т.е. берём текст текущего абзаца - `x.text`, запихиваем его в функцию `len` (сокращение от length), которая позволяет нам узнать длину нашего абзаца (если он пустая строка, то `len(x.text) = 0`, если нет, то `len(x.text) != 0`, т.е. длина любая, но не 0).

Если условие `if len(x.text) != 0` выполняется, то мы оставляем (или добавляем заново) данный абзац. Если же условие не выполнено и абзац - это пустая срока, мы его пропускаем и не добавляем снова к себе в список. Тут я надеюсь, тебе стало чуть проще от этого страшного выражения `[x for x in all_paras if len(x.text) != 0]` 	:wink:

**5**. Фух, избавились мы от проблемы, связанной с пустыми абзацами. Это успех! Давай ещё разок глянем на абзацы, которые у нас остались?

Тот же самый код для вывода абзацев, как и ранее:

![image](https://user-images.githubusercontent.com/46136468/142815662-98c3a347-af0a-461c-994b-a76d7a618c54.png)

Но в этот раз мы получим следующее:

![image](https://user-images.githubusercontent.com/46136468/142739652-cfc6b662-e513-4121-9b58-2b3e35331888.png)

С ума сойти, да это работает!!! 	:star_struck:

**6**. Помнишь, я пытался объяснить тебе, что я могу обратиться к списку и получить его элемент? Напомню: список можно представить как набор чисел от 1 до 5: `a = [1, 2, 3, 4, 5]`. Тут числа - это значения списка `a`, к которым мы можем обраться вот так: `a[0] = 1, a[2] = 3` (забыл сказать, все значения списка или массива начинают своё нумерование с 0!)

У нас же есть список всех абзацев, который хранится в переменной `all_paras`. Его можно представить вот так: `all_paras = [абзац 1, абзац 2, абзац 3, ..., абзац n]`. Если я напишу следующий код: `all_paras[1]`, то получу второй элемент нашего списка, т.е. абзац 2 (иначе говоря, `all_paras[1] = абзац 2`). 

Пожалуйста, не забывай, что программисты отличаются от людей и **начинают счёт с 0**. Именно из-за этого мы получаем абзац 2 вместо абзаца 1, ибо решили посмотреть, что лежит на второй позиции списка (хотя мы и запросили `all_paras[1]`, не надо забывать, что первым всё же является `all_paras[0] = абзац 1`)

**7**. Вроде всё тип-топ, но как нам вывести абзац, который хочет получить пользователь?

Для этого попросим господина или даму ввести число, которое будет характеризовать для нас номер абзаца из числа всех абзацев нормативно-правового-чего-то-там:

![image](https://user-images.githubusercontent.com/46136468/142739928-2afb6853-cc0a-4af6-97f8-dbb8cb8e2927.png)

Пусть это будет переменная `number`. Допустим, пользователь ввёл число 4 и захотел увидеть следующий абзац:

![image](https://user-images.githubusercontent.com/46136468/142739958-abe7b69e-b922-4844-b402-695ea11d65c4.png)

Как нам выдать пользователю то, что он хочет? Очень просто - давай обратимся к нашему списку по числу `number` (для этого считаем переменную с помощью `int(input())`, где `int()` - преобразование чего-либо к числовому типу, `input()` - считывание строки, которую вводит полизователь; число, которое мы считываем с помощью `input()` без `int(input())` является строкой и с ней невозможно работать, поэтому мы и используем перевод типа "строка" в тип "целое число": `int(input())`) и выведем текст, который хранится в переменной `all_paras[number]`. Для этого обратимся к `all_paras[number]` и с помощью метода `.text` получим текст, который хранится в этом (четвёртом, в нашем случае) абзаце. Выведем текст абзаца с помощью функции `print()`: `print(all_paras[number].text)`

![image](https://user-images.githubusercontent.com/46136468/142740675-10c9d722-ed7e-47cb-b202-3502f70e1dc8.png)

Получим:

![image](https://user-images.githubusercontent.com/46136468/142740017-673c19d0-ebd3-44b1-8ce3-7af9a20836da.png)

Ёлки-палки, это ведь не то, что нам нужно, нам нужен предыдущий абзац вообще-то... А блин, точно, я ведь обращаюсь к `all_paras[4]` и получаю нифига не абзац 4, а абзац 5, вот бы этим прогерам руки поотрывать! Так, ладно, работа над ошибками:

![image](https://user-images.githubusercontent.com/46136468/142740121-f4ad6ce6-d0ab-4452-af4e-43966cdead2d.png)

А теперь то что мы получим?

![image](https://user-images.githubusercontent.com/46136468/142740157-ad60b4ab-458e-43f0-b256-a427d54d4a0c.png)

Белиссимо! Теперь пользователь может получить любой интересный ему абзац, просто передавая нам число, которое обозначает номер абзаца!

**8**. Тут мы можем заняться бесконечной оптимизацией программы и её улучшениями, но я посчитал, что для тебя, с правфака, это будет сродни экзорцизму :grin:

## Итоги:

Мы смогли преобразовать файл с нормативным актом в список из абзацей, к которому мы можем обратиться с помощью номера абзаца, который интересен пользователю! Эта дичь будет фурычить со всеми похожими файлами, а если нет - мои соболезнования :D (пиши, помогу).

Вот как выглядит программа полностью (я обязательно её прикреплю, как файл):

![image](https://user-images.githubusercontent.com/46136468/142740433-c925d5d8-eacf-45d9-a7a8-159b4e383402.png)

Удачной защиты! 	:kissing_heart:
