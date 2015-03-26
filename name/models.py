#-*-coding:utf8;-*-
from django.db import models

NAME_GENDER_CHOICE = (                                                           
    (0, u'male'),                                                               
    (1, u'female'),                                                           
    (2, u'neutral'),                                                           
)     

class Name(models.Model):
    name = models.CharField('name', unique=True, max_length=16)
    cname = models.CharField('cname', max_length=16, null=True, blank=True)
    pronounce = models.CharField('pronounce', max_length=32, null=True, blank=True)
    gender = models.SmallIntegerField(choices=NAME_GENDER_CHOICE, db_index=True, default=0)
    rank = models.IntegerField('rank', default=0)
    description = models.TextField('description', null=True, blank=True)
    mp3 = models.FileField(upload_to='./mp3', blank=True)


    def __unicode__(self):
        return self.name

    def has_cname(self):
        if self.cname:
            return True
        else:
            return False

    def has_description(self):
        if self.description:
            return True
        else:
            return False

class Pinyin(models.Model):
    name = models.CharField('name', unique=True, max_length=16)
    roma = models.TextField('description', null=True, blank=True)


    def __unicode__(self):
        return self.name
