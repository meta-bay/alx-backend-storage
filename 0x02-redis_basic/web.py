#!/usr/bin/env python3
"""
Module for caching HTTP requests.
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cache_requests(fn: Callable) -> Callable:
    """ Decorator to cache the response of a URL and track call count.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - Checks if the URL's response is cached.
            - Tracks the number of times the URL is requested.
        """
        cache_client = redis.Redis()
        cache_client.incr(f'count:{url}')
        cached_response = cache_client.get(f'{url}')
        if cached_response:
            return cached_response.decode('utf-8')
        response = fn(url)
        cache_client.set(f'{url}', response, ex=10)
        return response
    return wrapper


@cache_requests
def get_page(url: str) -> str:
    """ Makes an HTTP GET request to the specified URL.
    """
    response = requests.get(url)
    return response.text
