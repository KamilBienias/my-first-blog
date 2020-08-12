# from django.db import models
#
#
# class Person(models.Model):
#     STATUS_CHOICES = (
#         ('available', 'Person available'),
#         ('overloaded', 'Person overloaded')
#     )
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     status = models.CharField(max_length=20,
#                               choices=STATUS_CHOICES,
#                               default='available')
#
#     def __str__(self):
#         return "Id: {} <br>"\
#                "First name: {} <br>" \
#                "Last name: {} <br>" \
#                "Person status: {} <br>" \
#                "Task set: {} <br><br>".format(self.id,
#                                               self.first_name,
#                                               self.last_name,
#                                               self.status,
#                                               self.task_set)
#
#
# class Task(models.Model):
#     person = models.ForeignKey(Person,
#                                on_delete=models.CASCADE,
#                                related_name='task_set')  # this related_name is default
#     summary = models.CharField(max_length=30)
#     description = models.CharField(max_length=200)
#     importance = models.DecimalField(max_digits=1, decimal_places=0)
#
#     def __str__(self):
#         return "Task: \"{}\" <br>" \
#                "with details: \"{}\" <br>" \
#                "has importance: {} (on a scale of 1 to 9) <br>" \
#                "is assigned to a person with id: \"{}\" named: {} {}<br><br>".format(
#                                                                    self.summary,
#                                                                    self.description,
#                                                                    self.importance,
#                                                                    self.person.id,
#                                                                    self.person.first_name,
#                                                                    self.person.last_name)
