import os

from assertpy import assert_that
from pylint import lint
from pylint.utils.linterstats import LinterStats


_CASES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cases')


class NonPluginRunner:
    def run(self, case_name: str) -> LinterStats:
        return lint.Run([os.path.join(_CASES_DIR, case_name)], exit=False).linter.stats


class PluginRunner:
    _PLUGIN_NAME = 'pylint_behave'

    def run(self, case_name: str) -> LinterStats:
        run = lint.Run([os.path.join(_CASES_DIR, case_name), f'--load-plugins={self._PLUGIN_NAME}'], exit=False)
        return run.linter.stats


class TestPluginCases(PluginRunner):
    def test_basic_class(self):
        stats = self.run('basic_class.py')

        assert_that(stats.global_note).is_equal_to(0)
        assert_that(stats.error).is_equal_to(1)

    def test_steps(self):
        stats = self.run('behave_steps.py')

        assert_that(stats.global_note).is_equal_to(10)

    def test_steps_with_errors(self):
        stats = self.run('behave_steps_with_errors.py')

        assert_that(stats.global_note).is_less_than(10)
        assert_that(stats.convention).is_equal_to(1)
        assert_that(stats.warning).is_equal_to(2)


class TestNonPluginCases(NonPluginRunner):
    def test_basic_class(self):
        stats = self.run('basic_class.py')

        assert_that(stats.global_note).is_equal_to(0)
        assert_that(stats.error).is_equal_to(1)

    def test_steps(self):
        stats = self.run('behave_steps.py')

        assert_that(stats.global_note).is_equal_to(0)
        assert_that(stats.error).is_greater_than(0)

    def test_steps_with_errors(self):
        stats = self.run('behave_steps_with_errors.py')

        assert_that(stats.global_note).is_equal_to(0)
        assert_that(stats.convention).is_greater_than(0)
        assert_that(stats.error).is_greater_than(0)
        assert_that(stats.warning).is_greater_than(0)
