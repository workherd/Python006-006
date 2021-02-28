from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User

class Orders(models.Model):
    """
    订单
    """
    __tablename__ = 'orders'
    order_stream_id = models.CharField(max_length=30, verbose_name='订单编号')
    body = models.CharField(max_length=60, verbose_name='订单内容', default='')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    # manager = models.ForeignKey('auth.User', related_name='manages', on_delete=models.CASCADE)
    is_effective = models.BooleanField(verbose_name='是否有效', default=True)

    class Meta:
        ordering = ['createtime']

    def __str__(self):
        return self.order_stream_id
