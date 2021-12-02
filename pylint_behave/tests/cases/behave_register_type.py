# pylint: disable=import-error,invalid-name
from behave import register_type, when


def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)


register_type(Number=parse_number)


@when('I add "{x:Number}" and "{y:Number}"')
def step_impl(context, x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
    context.calculator.add2(x, y)
