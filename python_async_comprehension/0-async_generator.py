#!/usr/bin/python3
import asyncio
import random
"function that will loop the coroutine 10 times "
async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
