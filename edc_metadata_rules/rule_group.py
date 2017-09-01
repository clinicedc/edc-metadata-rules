import sys

from django.apps import apps as django_apps
from django.core.management.color import color_style

style = color_style()


class RuleGroup:

    """Base class for CRF and Requisition rule groups.
    """

    @classmethod
    def get_rules(cls):
        return cls._meta.options.get('rules')

    @classmethod
    def validate(cls):
        """Outputs to the console if a target model referenced in a rule
        does not exist.
        """
        for rule in cls.get_rules():
            for target_model in rule.target_models:
                cls._lookup_model(model=target_model, category='target')

    @classmethod
    def _lookup_model(cls, model=None, category=None):
        sys.stdout.write(f'( ) {model}\r')
        try:
            django_apps.get_model(model)
        except LookupError:
            sys.stdout.write(style.ERROR(
                f'(?) {model}. See {category} model in {cls}\n'))
        else:
            sys.stdout.write(f'(*) {model}\n')
