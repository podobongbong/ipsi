from django.db import models

from university.models import *
from susi.models import YEARS


GUNS = (
        ('GA', '가군'),
        ('NA', '나군'),
        ('DA', '다군'),
        ('ETC', '군외'),
       )


class Jeongsi(models.Model):
    university = models.ForeignKey(
            verbose_name='대학',
            to='university.University',
            related_name='jeongsis',
            on_delete=models.CASCADE,
            )
    year = models.IntegerField(
            verbose_name='학년도',
            choices=YEARS,
            )

    def __str__(self):
        return str(self.year) + self.university.name + ' 정시전형'


class JeongsiDetail(models.Model):
    jeongsi = models.ForeignKey(
            verbose_name='정시전형',
            to='Jeongsi',
            on_delete=models.CASCADE,
            )
    major = models.ManyToManyField(
            verbose_name='학과',
            to=Major,
            )
    gun = models.CharField(
            verbose_name='군',
            choices=GUNS,
            max_length=7,
            )

    def __str__(self):
        return str(self.jeongsi.year) + '학년도 ' + self.jeongsi.university.name + ' 정시전형 (' + self.gun + ')'


class JeongsiSchedule(models.Model):
    jeongsi_detail = models.ForeignKey(
            verbose_name='정시전형 종류',
            to='JeongsiDetail',
            on_delete=models.CASCADE,
            )
    description = models.CharField(
            verbose_name='설명',
            max_length=255,
            )
    start_date = models.DateTimeField(
            verbose_name='시작시간',
            )
    end_date = models.DateTimeField(
            verbose_name='종료시간',
            )

    def __str__(self):
        return str(self.jeongsi_detail.jeongsi.year) + '학년도 '+ self.jeongsi_detail.jeongsi.university.name + '정시전형 (' + self.jeongsi_detail.gun + ') 일정: ' + self.description
