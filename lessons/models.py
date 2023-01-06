from django.db import models


class Lesson(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=500, blank=False)
    teacher = models.CharField(verbose_name='Учитель', max_length=255, blank=False)
    classroom = models.CharField(verbose_name='Аудитория', max_length=50, blank=False)

    started_at = models.DateTimeField(verbose_name='Дата/Время начала', blank=False)
    ended_at = models.DateTimeField(verbose_name='Дата/Время окончания', blank=False)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f"Урок '{self.title}' в аудитории № {self.classroom} от {self.started_at}"
