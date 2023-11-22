#!/usr/bin/env python3
"""function that take the code from wait_n and alter it into a new function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """script that return list"""
    tasks = []
    result_list = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    result_list = [await task for task in asyncio.as_completed(tasks)]
    return result_list
