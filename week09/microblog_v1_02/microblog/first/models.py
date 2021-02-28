from django.db import models

# Create your models here.

from datetime import datetime


class Articles(models.Model):
    """文章"""

    articleid = models.CharField(max_length=30,verbose_name='文章id', default='')
    article = models.CharField(max_length=30, verbose_name='文章内容')
    createtime = models.DateTimeField(auto_now_add=True)
    # 第一次执行migrate时要注释owner
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createtime']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # 保存时需要出发连带操作是需要定义
        super(Articles, self).save(*args, **kwargs)
