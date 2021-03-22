from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''Обычный пост'''
    user = models.ForeignKey(
        User, verbose_name="Пользователь", 
        related_name="posts", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField("Дата и время", auto_now_add=True)
    content = models.TextField("Контент", max_length=500)

    def __str__(self):
        return f"{self.user}'s post"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-timestamp"]

class Comment(models.Model):
    """Модель коментариев к новостям"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name="Новость", related_name="comments", on_delete=models.CASCADE
    )
    text = models.TextField("Сообщение", default='')
    parent = models.ForeignKey(
        "self",
        verbose_name="Родительский комментарий",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"