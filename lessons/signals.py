from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from lessons.models import Lesson
from lessons.tasks import send_notifications_to_channels_task


@receiver(post_save, sender=Lesson)
def send_notifications_to_channels(sender, **kwargs):
    lesson = kwargs.get('instance')
    created = kwargs.get('created')

    if created:
        send_notifications_to_channels_task.apply_async((
            f"Напоминание: Урок по дисциплине '{lesson.title}' в аудитории № {lesson.classroom}, пройдет ровно через 15 минут.",),
            eta=lesson.started_at - timedelta(minutes=15))


def send_class_schedule():
    pass  # todo add class schedule
