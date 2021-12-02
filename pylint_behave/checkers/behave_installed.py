from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages

from pylint_behave.__pkginfo__ import BASE_ERROR_ID


class BehaveInstalledChecker(BaseChecker):
    name = 'behave-installed-checker'

    msgs = {
        f'F{BASE_ERROR_ID}01': (
            'No module named "behave".',
            'behave-not-available',
            'behave could not be imported by the pylint-behave plugin.'
        ),
    }

    @check_messages('behave-not-available')
    def open(self) -> None:
        try:
            __import__('behave')
        except ImportError:
            self.linter.set_current_module('pylint_behave')
            self.add_message('behave-not-available')
