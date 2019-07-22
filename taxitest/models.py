from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.CharField(primary_key=True, max_length=32)
    current_position_x = models.FloatField(blank=True, null=True)
    current_position_y = models.FloatField(blank=True, null=True)
    current_velocity = models.FloatField(blank=True, null=True)
    tire_pressure_left_front = models.FloatField(blank=True, null=True)
    tire_pressure_right_front = models.FloatField(blank=True, null=True)
    tire_pressure_left_behind = models.FloatField(blank=True, null=True)
    tire_pressure_right_behind = models.FloatField(blank=True, null=True)
    camera_status = models.NullBooleanField()
    lidar_status = models.NullBooleanField()
    ibeo_status = models.NullBooleanField()

    CAR_STATUS_CHOICES = (
        ('m','Maintenance'),
        ('a','Available'),
        ('r','Running'),
    ) 
    car_status = models.CharField(max_length=1, choices=CAR_STATUS_CHOICES, blank=True, default='m')
    route = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.car_id

class Client(models.Model):
    client_name = models.CharField(max_length=10)
    phone_number = models.CharField(primary_key=True,max_length=11)
    password = models.CharField(max_length=128)
    login_or_create = models.NullBooleanField()

    def __str__(self):
        return '%s, %s' % (self.client_name, self.phone_number)

class Order(models.Model):
    order_id = models.CharField(primary_key=True,max_length=11)
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    phone_number = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    start_position_x = models.FloatField(blank=True, null=True)
    start_position_y = models.FloatField(blank=True, null=True)
    target_position_x = models.FloatField(blank=True, null=True)
    target_position_y = models.FloatField(blank=True, null=True)

    is_car_arrive_start = models.NullBooleanField()
    is_in_car = models.NullBooleanField()
    is_car_reach_target = models.NullBooleanField()
    is_car_start_to_start_point = models.NullBooleanField()

    ORDER_STATUS_CHOICES = (
        ('p','Preparing'),
        ('f','Finished'),
        ('r','Running'),
    )
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, blank=True, default='p')
    order_creation_time = models.DateTimeField()
    order_end_time =  models.DateTimeField(blank=True, null=True)
    order_amount = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ["order_creation_time"]

    def __str__(self):
        return self.order_id