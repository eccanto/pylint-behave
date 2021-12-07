from astroid import nodes
from pylint.checkers.base import BasicErrorChecker
from pylint.checkers.variables import VariablesChecker
from pylint.lint.pylinter import PyLinter

from pylint_plugin_utils import suppress_message


_BEHAVE_STEP_IMPL_NAME = 'step_impl'

_BEHAVE_NAMES = [
    'step',
    'given',
    'when',
    'then',
    'Step',
    'Given',
    'When',
    'Then',
]


def is_behave_func_redefined(node: nodes.Module) -> bool:
    return node.name == _BEHAVE_STEP_IMPL_NAME


def is_name_in_behave(node: nodes.Module) -> bool:
    if hasattr(node, 'modname') and (node.modname == 'behave'):
        node.names = [(name, alias) for name, alias in node.names if name not in _BEHAVE_NAMES]

    return False


def apply_augmentations(linter: PyLinter) -> None:
    """Apply augmentation and suppression rules."""
    suppress_message(
        linter, BasicErrorChecker.visit_functiondef, 'function-redefined', is_behave_func_redefined
    )
    suppress_message(
        linter, VariablesChecker.visit_import, 'no-name-in-module', is_name_in_behave
    )
    suppress_message(
        linter, VariablesChecker.visit_importfrom, 'no-name-in-module', is_name_in_behave
    )
