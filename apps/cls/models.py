from django.db import models
from ckeditor.fields import RichTextField


class BranchImage(models.Model):
    image = models.ImageField(upload_to="images/branch_images", verbose_name="Изображение")
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='images', verbose_name='Филиал')

    def __str__(self):
        return self.image.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''


class Region(models.Model):
    name = models.CharField(max_length=20, verbose_name='Районы города Бишкек', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=False)
    description = RichTextField(verbose_name="Описание про библиотеку", blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Район")
    address = models.CharField(max_length=100, verbose_name='Адрес', blank=False)
    time_work = models.CharField(max_length=100, verbose_name='Время работы', blank=False)
    video_link = models.CharField(max_length=100, verbose_name='Видео ссылка', blank=True)
    audio = models.FileField(upload_to='audio/', verbose_name='Аудио', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, verbose_name="Рейтинг")
    num_votes = models.PositiveIntegerField(default=0, verbose_name="Количество голосов")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(verbose_name="Активный", default=True)

    def __str__(self):
        return self.name

    def update_rating(self, new_rating):
        total_rating = self.rating * self.num_votes
        total_rating += new_rating
        self.num_votes += 1
        self.rating = total_rating / self.num_votes
        self.save()

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
