# pylint: disable=import-error
from behave import step, given, when, then, Step, Given, When, Then


@step('step 1')
def step_impl():
    import os

    x = 2# invalid comment


@Step('Step 2')
def step_impl():
    pass
