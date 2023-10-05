from unittest.mock import MagicMock

def my_func(keyword_callback, n):
    '''function for unittest'''
    for _ in range(n):
        keyword_callback()

mock_callback = MagicMock()

my_func(keyword_callback=mock_callback, n=10)

assert mock_callback.call_count == 10
