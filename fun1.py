from datetime import datetime
from functools import singledispatch


@singledispatch
def report(value):
    return f'Bez określania typu: {value}'


@report.register
def _(value: datetime):
    return f'Obiekt datetime: {value.isoformat()}'
