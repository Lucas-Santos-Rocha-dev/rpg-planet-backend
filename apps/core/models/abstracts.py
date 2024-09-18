import uuid as uuid

from django.db import models


class HasName(models.Model):
    name = models.CharField("Nome", max_length=160)

    class Meta:
        abstract = True


class HasCreatedIn(models.Model):
    create_in = models.DateTimeField("Criado em", editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class HasChangedIn(models.Model):
    changed_in = models.DateTimeField("Alterado em", editable=False, auto_now=True)

    class Meta:
        abstract = True


class HasExternalKey(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @classmethod
    def by_uuid(cls, uuid_parameter):
        return cls.objects.get(uuid=uuid_parameter)

    class Meta:
        abstract = True


class Base(HasExternalKey, HasCreatedIn, HasChangedIn, HasName):
    # Expoe explicitamente o model manager para evitar falsos alertas de Unresolved attribute reference for class Model
    objects = models.Manager()

    @classmethod
    def by_id(cls, id_parameter):
        return cls.objects.get(id=id_parameter)

    class Meta:
        abstract = True


class BaseWithoutName(HasExternalKey, HasCreatedIn, HasChangedIn):
    # Expoe explicitamente o model manager para evitar falsos alertas de Unresolved attribute reference for class Model
    objects = models.Manager()

    @classmethod
    def by_id(cls, id_parameter):
        return cls.objects.get(id=id_parameter)

    class Meta:
        abstract = True
