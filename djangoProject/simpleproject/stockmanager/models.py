from django.db import models
# Need to add save features

class Item(models.Model):

    item_name = models.CharField(max_length=200)
    article_number = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name

class Location(models.Model):

    f_num = models.CharField(max_length=2,default=0)
    m_num = models.CharField(max_length=1,default=0)
    l_num = models.CharField(max_length=1,default=0)
    contained_items = models.ManyToManyField(StockedItem, blank=True)
    
    def __str__(self):
        return "F.{} M.{} L.{}".format(self.f_num,self.m_num,self.l_num)
    
    def intList(self):
        return [int(self.f_num),int(self.m_num),int(self.l_num)]
