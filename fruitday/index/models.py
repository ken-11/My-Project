from django.db import models

# Create your models here.


class Users(models.Model):
  uphone = models.CharField(max_length=11)
  upass = models.CharField(max_length=18)
  uname = models.CharField(max_length=30, default='匿名')
  uemail = models.EmailField(null=True)
  isActive = models.BooleanField(default=True)

  def __str__(self):
    return self.uname

  class Meta:
    verbose_name = '用户'
    verbose_name_plural = verbose_name

# 商品类型


class GoodsType(models.Model):
  # 1.类别名称
  title = models.CharField(max_length=30)
  # 2.类别描述
  desc = models.TextField(null=True)
  # 3.类别图片
  picture = models.ImageField(upload_to='static/upload/goodsType')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = '商品类别'
    verbose_name_plural = verbose_name


# 商品信息
class Goods(models.Model):
  # 1.商品名称
  title = models.CharField(max_length=30, verbose_name='商品标题')
  # 2.商品价格
  price = models.DecimalField(
      max_digits=7, decimal_places=2, verbose_name='商品价格')
  # 3.商品规格
  spec = models.CharField(max_length=30, verbose_name='商品规格')
  # 4.商品图片
  picture = models.ImageField(
      upload_to='static/upload/goods', verbose_name='商品图片')
  # 6.增加对 GoddsType的引用(一对多)
  goodsType = models.ForeignKey(GoodsType, null=True,verbose_name='商品类型')
  # 5.商品状态
  isActive = models.BooleanField(default=True, verbose_name='销售中')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = '商品'
    verbose_name_plural = verbose_name
