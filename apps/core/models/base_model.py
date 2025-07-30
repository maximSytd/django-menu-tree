import typing

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CreationDateTimeField(models.DateTimeField):
    """
    CreationDateTimeField

    By default, sets editable=False, blank=True, auto_now_add=True
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("editable", False)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("auto_now_add", True)
        models.DateTimeField.__init__(self, *args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.editable is not False:
            kwargs["editable"] = True
        if self.blank is not True:
            kwargs["blank"] = False
        if self.auto_now_add is not False:
            kwargs["auto_now_add"] = True
        return name, path, args, kwargs


class ModificationDateTimeField(CreationDateTimeField):
    """
    ModificationDateTimeField

    By default, sets editable=False, blank=True, auto_now=True

    Sets value to now every time the object is saved.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("auto_now", True)
        models.DateTimeField.__init__(self, *args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.auto_now is not False:
            kwargs["auto_now"] = True
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        if not getattr(model_instance, "update_modified", True):
            return getattr(model_instance, self.attname)
        return super().pre_save(model_instance, add)


class TimeStampedModel(models.Model):
    """
    TimeStampedModel

    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """

    created = CreationDateTimeField(_("created"))
    modified = ModificationDateTimeField(_("modified"))

    def save(self, **kwargs):
        self.update_modified = kwargs.pop(
            "update_modified", getattr(self, "update_modified", True)
        )
        super().save(**kwargs)

    class Meta:
        get_latest_by = "modified"
        abstract = True


class BaseModel(TimeStampedModel):
    """Base model for apps' models.

    This class adds to models created and modified fields

    """

    class Meta:
        abstract = True

    def clean(self) -> None:
        """Validate model data.

        First we collect all errors as dict and then if there any errors, we
        pass them ValidationError and raise it. By doing this django admin and
        drf can specify for each field an error.

        """
        super().clean()
        errors = {}
        for field in self._meta.fields:
            clean_method = f"clean_{field.name}"
            if hasattr(self, clean_method):
                try:
                    getattr(self, clean_method)()
                except ValidationError as error:
                    errors[field.name] = error
        if errors:
            raise ValidationError(errors)


BaseModelAncestor = typing.TypeVar("BaseModelAncestor", bound=BaseModel)
