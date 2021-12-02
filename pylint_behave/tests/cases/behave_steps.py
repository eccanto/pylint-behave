# pylint: disable=import-error
from behave import step, given, when, then, Step, Given, When, Then


@step('step 1')
def step_impl():
    pass


@Step('Step 2 - title case')
def step_impl():
    pass


@given('given 1')
def step_impl():
    pass


@Given('Given 2 - title case')
def step_impl():
    pass


@when('when 2')
def step_impl():
    pass


@When('When 2 - title case')
def step_impl():
    pass


@then('then 3')
def step_impl():
    pass


@Then('Then 3 - title case')
def step_impl():
    pass
