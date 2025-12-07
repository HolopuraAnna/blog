from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from blog.models import Comment


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Створення груп
    author_group, created = Group.objects.get_or_create(name='Author')
    moderator_group, created = Group.objects.get_or_create(name='Moderator')

    # Отримуємо permissions для моделі Comment
    comment_ct = ContentType.objects.get_for_model(Comment)

    # Автор: може додавати, змінювати, видаляти ТІЛЬКИ свої коментарі
    author_permissions = [
        Permission.objects.get(codename='add_comment'),
        Permission.objects.get(codename='change_comment'),
        Permission.objects.get(codename='delete_comment'),
    ]

    # Додати ці права групі автора
    author_group.permissions.set(author_permissions)

    # Модератор: має всі права автора + може видаляти будь-який коментар
    moderator_permissions = author_permissions + [
        Permission.objects.get(codename='delete_comment'),
    ]

    moderator_group.permissions.set(moderator_permissions)
