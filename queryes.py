import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)

    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)

    # exact, iexact -- точный, безошибочный

    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))

    # contains, icontains -- содержит, содержит иконку

    # print(Entry.objects.filter(headline__contains='мод'))

    # in - Проверка вхождения

    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # <QuerySet [<Entry: Изучение красот Мачу-Пикчу>, <Entry: Знакомство с Парижем>, <Entry: Открывая тайны Колизея>]>

    # print(Entry.objects.filter(number_of_comments__in='123'))
    # число комментариев 1 или 2 или 3

    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)

    # gt, gte, lt, lte
    # Больше чем; Больше равно чем; Меньше чем; Меньше равно чем.

    # Вывести все записи, у которых число комментарием больше 10
    # print(Entry.objects.filter(number_of_comments__gt=10))

    # Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
    # import datetime
    # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))

    # Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))

    # Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
    # print(Entry.objects.filter(headline__lte="Зя"))

    # startswith, istartswith, endswith, iendswith
    # Начинается с(с / без учета регистра),
    # заканчивается на(с / без учета регистра).

    # print(Entry.objects.filter(headline__startswith='Как'))
    # print(Entry.objects.filter(headline__endswith='ния'))

    # range - Диапазон проверки(включительно).
    import datetime

    # start_date = datetime.date(2023, 1, 1)
    # end_date = datetime.date(2023, 12, 31)
    # print(Entry.objects.filter(pub_date__range=(start_date, end_date)))

    # При данной постановке задачи (вывод за конкретный год) будет проще воспользоваться __year результат будет аналогичен
    # print(Entry.objects.filter(pub_date__year=2023))

    # entries = Entry.objects.filter(pub_date__year=2023)
    # for entry in entries:
    #     print(entry)

    # year, month, day, week, week_day, quarter, hour, minute, second
    # Для полей даты и даты и времени точное совпадение:
    # print(Entry.objects.filter(pub_date__year__lt=2022))

    # Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
    # entries = Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline')
    # for entry in entries:
    #     print(entry)

    # Вывести username авторов у которых есть публикации с 1 по 15 апреля 2023 года,
    # вывести без использования range. Пример для работы с __day
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
    #     pub_date__day__lte=15).values_list("author__name").distinct())
    # Сначала отфильтровываем по году, затем по дням,
    # затем получаем значения имен у авторов и говорим, чтобы не было повторов

    # Вывести статьи опубликованные в понедельник (так как datetime работает по американской системе,
    # то начало недели идёт с воскресенья, а заканчивается субботой, поэтому понедельник второй день в неделе)
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))

    # date, time
    # Для полей даты и времени преобразует значение как дату или время.
    # Нужно быть внимательным так как __date и __time не применить к полям
    # типа DateField, только к DateTimeField

    # Вывод всех записей по конкретной дате
    # print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))

    # Вывод всех записей новее конкретной даты
    # print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))

    # Вывод записей по конкретному времени
    # print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))

    # isnull
    # Принимает True или False,
    # которые соответствуют SQL-запросам IS NULL и IS NOT NULL, соответственно
    # print(AuthorProfile.objects.filter(city__isnull=True))

    # regex, iregex
    # Чувствительное/нечувствительное к регистру совпадение регулярного выражения.
    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))

    # Слова, содержащие «стран» (с границами слов)
    # print(Entry.objects.filter(body_text__regex=r'\bстран\w*\b'))

    # Вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))

    # Если необходимо вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru,
    # но чтобы значения не повторялись, то используем distinct()
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())


    # Применяемые методы для формирования запроса


    # all() - Вывод всех значений в таблице objects.all()
    # all_obj = Blog.objects.all()
    # print("Вывод всех значений в таблице Blog\n", all_obj)

    # first() - Вывод первого значения objects.first()
    # all_obj = Blog.objects.first()
    # print("Вывод первого значения в таблице Blog\n", all_obj)


    # Последовательность запросов
    # all_obj = Blog.objects.all()
    # obj_first = all_obj.first()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #       f"Все значения = {all_obj}")

    # Итерируемость
    # Объект QuerySet итерируемый,
    # а значит есть возможность обращения через [] и слайсирование, for и т.д
    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(all_obj[0])  # Получение 0-го элемента
    # print(all_obj[2:4])  # Получение 2 и 3 элемента
    """Получение последнего элемента не осуществимо через обратный индекс
    all_obj[-1] - нельзя
    можно воспользоваться latest('<name_field>'), где <name_field> - имя колонки в БД.

    Почти все операции над БД не требуют предварительного получения всех элементов,
    постоянная запись Blog.objects.all() просто для примера.
    """
    # print(all_obj.latest("id"))  # Получение последнего элемента
    # print(Blog.objects.latest("id"))  # Одинаково работает

    # print(Blog.objects.count())  # Можно ко всей таблице
    # print(Blog.objects.filter(id__gte=2).count())  # Можно к запросу
    # all_data = Blog.objects.all()
    # filtred_data = all_data.filter(id__gte=2)
    # print(filtred_data.count())  # Можно к частным запросам

    print(Author.objects.annotate(article_count=Count('entries')).order_by('-article_count').first())
