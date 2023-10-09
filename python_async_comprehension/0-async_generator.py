#!/usr/bin/env python3
"""The coroutine will loop 10 times, each time asynchronously wait 1 second"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function that will loop the coroutine 10 times """
    for i in range(10):
        """Asynchronously wait for 1 second"""

        await asyncio.sleep(1)
        """The coroutine will loop 10 times"""
        yield random.uniform(0, 10)
