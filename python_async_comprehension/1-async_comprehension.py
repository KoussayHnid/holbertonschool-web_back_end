#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension."""
    return [i async for i in async_generator()]

async def main():
    random_numbers = await async_comprehension()
    print(random_numbers)
