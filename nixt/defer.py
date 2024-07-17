# This file is placed in the Public Domain.
# pylint: disable=R0903,W0125,W0622,E1102


"deferred exception handling."


import io
import traceback


from .object import Object, add, values


class Errors(Object):

    "Errors"

    out    = None


def all():
    "return all errors."
    for exc in values(Errors):
        if isinstance(exc, Exception):
            yield exc


def errors():
    "show exceptions"
    for exc in all():
        output(exc)


def format(exc):
    "format an exception"
    res = ""
    stream = io.StringIO(
                         traceback.print_exception(
                                                    type(exc),
                                                    exc,
                                                    exc.__traceback__
                                                  )
                        )
    for line in stream.readlines():
        res += line + "\n"
    return res


def later(exc):
    "add an exception"
    excp = exc.with_traceback(exc.__traceback__)
    excp.__name__ = str(type(excp))
    add(Errors, excp)


def output(exc):
    "check if output function is set."
    if Errors.out:
        Errors.out(format(exc))


def __dir__():
    return (
        'Errors',
        'errors',
        'later'
    )
