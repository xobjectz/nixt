# This file is placed in the Public Domain.
# pylint: disable=R0903


"caching"


from .object import Object


class Cache(Object):

    "Cache"


def __dir__():
    return (
        'Broker',
    )
