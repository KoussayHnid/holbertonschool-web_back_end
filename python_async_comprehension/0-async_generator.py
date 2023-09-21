#!/usr/bin/env python3
import asyncio
import random

async def async_generator() -> Generator(floot, None, None):
    "function that will loop the coroutine 10 times "
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
