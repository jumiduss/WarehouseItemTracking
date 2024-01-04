from django.db import models
# Need to add save features

class Location(models.Model):

    f_num = models.CharField(max_length=2)
    m_num = models.CharField(max_length=1,default=0)
    l_num = models.CharField(max_length=1,default=0)
    
    class Meta:
        ordering = ["f_num","m_num","l_num"]

    def __str__(self):
        return "F.{} M.{} L.{}".format(self.f_num,self.m_num,self.l_num)
    
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    article_number = models.CharField(max_length=6,default="0")
    locations = models.ManyToManyField(Location)

    class Meta:
        ordering = ["item_name"]

    def __str__(self):
        return self.item_name

