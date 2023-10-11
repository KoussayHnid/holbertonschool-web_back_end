#!/usr/bin/env python3
"""function that takes an integer and return a asyncio"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """script that returns an asyncio"""
    return asyncio.create_task(wait_random(max_delay))
