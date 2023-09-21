#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    "function that will loop the coroutine 10 times "
    for _ in range(10):
        "Asynchronously wait for 1 second"

        await asyncio.sleep(1)
        "The coroutine will loop 10 times"

        yield random.randint(0, 10)
