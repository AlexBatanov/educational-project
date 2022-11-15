from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    # для фото нужна настройка MEDIAROOT
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
