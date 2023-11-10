from django.db import models
from django.contrib.auth.models import User


class InformationComponent(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='components', on_delete=models.CASCADE)

    linked_components = models.ManyToManyField(
        'self',
        through='ComponentLink',
        symmetrical=False,
        related_name='linked_to'
    )

    def __str__(self):
        return self.title

    def link_to(self, other_component):
        ComponentLink.objects.create(
            from_component=self,
            to_component=other_component
        )


class ComponentLink(models.Model):
    from_component = models.ForeignKey(InformationComponent, related_name='from_links', on_delete=models.CASCADE)
    to_component = models.ForeignKey(InformationComponent, related_name='to_links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_component', 'to_component')


class Idea(InformationComponent):
    description = models.TextField()


class Deadline(InformationComponent):
    due_date = models.DateTimeField()

