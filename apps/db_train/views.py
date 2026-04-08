from django.shortcuts import render
from django.views import View
from pygments.lexer import default

from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):

        # Создайте здесь запросы к БД

        # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        # TODO Какой автор имеет наибольшее количество опубликованных статей?


        # Находим автора с наибольшим числом статей
        self.answer2 = Author.objects.annotate(article_count=Count('entries')).order_by('-article_count').first()

        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка']).distinct()

        # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender='ж').count()

        # TODO Какой процент авторов согласился с правилами при регистрации?
        total_authors = Author.objects.count()
        agreed_authors = Author.objects.filter(status_rule=True).count()
        self.answer5 = round(agreed_authors / total_authors * 100) if total_authors > 0 else 0

        # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1,5)).distinct()

        # TODO Какой автор имеет наибольший возраст?
        self.answer7 = Author.objects.order_by('-age').first()

        # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.exclude(phone_number__isnull=True).exclude(
            phone_number='').count()

        # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lt=25)

        # TODO Сколько статей написано каждым автором?
        # self.answer10 = Author.objects.annotate(
        #     article_count=Count('entries'))

        self.answer10 = Author.objects.annotate(number_of_entries=Count('entries')).values('username', 'number_of_entries')




        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
