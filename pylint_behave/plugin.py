"""Common Pylint Behave module."""
from pylint.checkers.base import NameChecker
from pylint.lint.pylinter import PyLinter
from pylint_plugin_utils import get_checker

from pylint_behave import compat
from pylint_behave.augmentations import apply_augmentations
from pylint_behave.checkers import register_checkers


def load_configuration(linter: PyLinter) -> None:
    """
    Amend existing checker config.
    """
    name_checker = get_checker(linter, NameChecker)
    name_checker.config.good_names += ('i', 'j', 'x', 'y')


def register(linter: PyLinter) -> None:
    """
    Registering/Configuring checkers.
    """
    register_checkers(linter)
    apply_augmentations(linter)

    if not compat.LOAD_CONFIGURATION_SUPPORTED:
        load_configuration(linter)
