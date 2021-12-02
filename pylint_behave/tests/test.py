import os

from assertpy import assert_that
from pylint import lint
from pylint.utils.linterstats import LinterStats


class PylintRunner:
    _PLUGIN_NAME = 'pylint_behave'
    _CASES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cases')

    def run(self, case_name: str) -> LinterStats:
        run = lint.Run(
            [os.path.join(self._CASES_DIR, case_name), f'--load-plugins={self._PLUGIN_NAME}'],
            exit=False
        )
        return run.linter.stats


class TestBehaveCase(PylintRunner):
    def test_steps(self):
        stats = self.run('behave_steps.py')

        assert_that(stats.global_note).is_equal_to(10)

    def test_register_type(self):
        stats = self.run('behave_register_type.py')

        assert_that(stats.global_note).is_equal_to(10)


class TestNonBehaveCase(PylintRunner):
    def test_basic_class(self):
        stats = self.run('basic_class.py')

        assert_that(stats.error).is_equal_to(1)
        assert_that(stats.global_note).is_equal_to(0)
