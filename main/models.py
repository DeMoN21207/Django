from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=30)
    sourname = models.CharField('Фамилия', max_length=40)
    middlename = models.CharField('Отчество', max_length=40)
    login = models.CharField('Логин', max_length=15, unique=True)
    password = models.CharField('Пароль', max_length=15)


    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Логин'
        verbose_name_plural = 'Логины'


class ListSource(models.Model):
    namesourse = models.CharField('Имя', max_length=50)
    urlSource = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.namesourse

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Author(models.Model):
    Author = models.CharField("Автор", max_length=50)

    def __str__(self):
        return self.Author

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Article(models.Model):
    urlArticle = models.CharField(max_length=100, unique=True)
    descripion = models.TextField('Описание статьи')
    nameofarticle = models.TextField('Название статьи', max_length=150)

    def __str__(self):
        return self.nameofarticle

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class RecommendArticle(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)




class Query(models.Model):
    findQuery = models.ForeignKey(Person, on_delete=models.CASCADE, default=0,related_name="Person")
    ResultOfQuery = models.ForeignKey(RecommendArticle, on_delete=models.CASCADE)

    def __str__(self):
        return self.findQuery

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
