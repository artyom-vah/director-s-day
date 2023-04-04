from django.db import models


DIVISION_CHOICES = (
    ('Топливный', 'Топливный'),
    ('Машиностроение', 'Машиностроение'),
    ('ЯОК', 'ЯОК'),
    ('Энергетический', 'Энергетический'),
)


class Division(models.Model):
    '''Модель для дивизионов'''
    name = models.CharField(max_length=20, choices=DIVISION_CHOICES, verbose_name='Название дивизиона')

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизионы'

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    '''Модель для предприятий'''
    name = models.CharField(max_length=50, blank=True, verbose_name='Название предприятия')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Название дивизиона')

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    def __str__(self):
        return self.name


class Question(models.Model):
    '''Модель для вопросов'''
    date_time = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
    enterprise = models.ForeignKey(Enterprise, blank=True, on_delete=models.CASCADE, verbose_name='Предприятие')
    question = models.TextField(verbose_name='Вопрос')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question

