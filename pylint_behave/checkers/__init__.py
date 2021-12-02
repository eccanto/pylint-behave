from pylint.lint.pylinter import PyLinter

from pylint_behave.checkers.behave_installed import BehaveInstalledChecker


def register_checkers(linter: PyLinter) -> None:
    """Register checkers."""
    linter.register_checker(BehaveInstalledChecker(linter))
