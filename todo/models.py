from django.db import models


class Person(models.Model):
    STATUS_CHOICES = (
        ('available', 'Person available'),
        ('overloaded', 'Person overloaded')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='available')

    def __str__(self):
        return f"Id number: {self.id}, first name: {self.first_name}, last name: {self.last_name}, status: {self.status}"

    def __repr__(self):
        return "<br>"\
               "Id number: {0} <br> " \
               "First name: {1} <br> " \
               "Last name: {2} <br> " \
               "Person status: {3} <br> " \
               "Task set: {4} <br><br>".format(self.id,
                                               self.first_name,
                                               self.last_name,
                                               self.status,
                                               self.task_set)


class Task(models.Model):
    person = models.ForeignKey(Person,
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='task_set')  # this related_name is default
    summary = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    importance = models.DecimalField(max_digits=1, decimal_places=0)

    # def __str__(self):
    #     return "Task: \"{}\" <br>" \
    #            "with details: \"{}\" <br>" \
    #            "has importance: {} (on a scale of 1 to 9) <br>" \
    #            "is assigned to a person with id: \"{}\" named: {} {}<br><br>".format(
    #                                                                self.summary,
    #                                                                self.description,
    #                                                                self.importance,
    #                                                                self.person.id,
    #                                                                self.person.first_name,
    #                                                                self.person.last_name)

    def __str__(self):
        return "Task: \"{}\" " \
               "with details: \"{}\" " \
               "has importance: {} (on a scale of 1 to 9)".format(
            self.summary,
            self.description,
            self.importance)


    # def __repr__(self):
    #     return "<br>"\
    #            "Id number: {0} <br> " \
    #            "Task: \"{1}\" <br>" \
    #            "with details: \"{2}\" <br>" \
    #            "has importance: {3} (on a scale of 1 to 9) <br>" \
    #            "is assigned to a person with id: \"{4}\" named: {5} {6}<br><br>".format(
    #             self.id,
    #             self.summary,
    #             self.description,
    #             self.importance,
    #             self.person.id,
    #             self.person.first_name,
    #             self.person.last_name)

    def __repr__(self):
        return "<br>" \
               "Id number: {0} <br> " \
               "Task: \"{1}\" <br>" \
               "with details: \"{2}\" <br>" \
               "has importance: {3} (on a scale of 1 to 9) <br><br>".format(
            self.id,
            self.summary,
            self.description,
            self.importance)
