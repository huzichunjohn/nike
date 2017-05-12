from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import IntegrityError, models, transaction
from bitfield import BitField

class MyModel(models.Model):
    flags = BitField(flags=(
        'awesome_flag',
        'flaggy_foo',
        'baz_bar',
    ))

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    depends_on = models.ManyToManyField('self', through='ApplicationDependency',
                                          related_name='used_by',
                                          symmetrical=False)

    def __str__(self):
        return 'Application {}'.format(self.name)

    def get_application_by_depends_on(self):
        result = []
        application_ids = ApplicationDependency.objects.filter(from_application=self).values_list('to_application', flat=True)
        for application_id in application_ids:
            application = Application.objects.get(id=application_id)
            result.append(application.name)
        return result

    def get_appplication_by_used_by(self):
        result = []
        application_ids = ApplicationDependency.objects.filter(to_application=self).values_list('from_application', flat=True)
        for application_id in application_ids:
            application = Application.objects.get(id=application_id)
            result.append(application.name)
        return result

    def add_application_by_depends_on(self, application):
        try:
            with transaction.atomic():
                ApplicationDependency.objects.create(from_application=self, to_application=application)
        except IntegrityError:
            pass

    def remove_application_by_depends_on(self, application):
        try:
            with transaction.atomic():
                ApplicationDependency.objects.filter(from_application=self, to_application=application).delete()
        except IntegrityError:
            pass

class ApplicationDependency(models.Model):
    from_application = models.ForeignKey(Application, related_name='from_application')
    to_application = models.ForeignKey(Application, related_name='to_application')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('from_application', 'to_application'),)

    def __str__(self):
        return '{} depends on {}'.format(self.from_application, self.to_application)
