from django.db import models


class User(models.Model):
    user_email = models.CharField(max_length=30, unique=True)
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_email


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    before_test = models.CharField(max_length=100)
    module1_advantages = models.CharField(max_length=300)
    module1_obstacles = models.CharField(max_length=300)
    module1_extra = models.CharField(max_length=100)
    module2_selections = models.CharField(max_length=100)
    module2_extra_need = models.CharField(max_length=100)
    module3_selections = models.CharField(max_length=100)
    module3_extra_value = models.CharField(max_length=100)
    module4_selections_1 = models.CharField(max_length=100)
    module4_selections_2 = models.CharField(max_length=100)
    module5_personal = models.CharField(max_length=100)  # '' = not selected, 0 = true, 1 = false
    module5_work = models.CharField(max_length=100)
    module5_personal_selections = models.CharField(max_length=100)
    module5_work_selections = models.CharField(max_length=100)
    module6_selections = models.CharField(max_length=100)
    after_test = models.CharField(max_length=100)
    finished = models.CharField(max_length=100)
    current = models.IntegerField(default=0)  # 0-6
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.user.user_email + ' ' + str(self.date.day) + '/' + str(self.date.month) + '/' + str(self.date.year)





