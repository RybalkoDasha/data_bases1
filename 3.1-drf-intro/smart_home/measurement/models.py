from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurments(models.Model):
    temperature = models.DecimalField(max_digits=2,
                                      decimal_places=1,
                                      verbose_name='температура')
    created_at = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
