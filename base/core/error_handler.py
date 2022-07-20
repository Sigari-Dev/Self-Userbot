def _error(func):
    async def inner_function(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception as ex:
            await args[1].edit(f"[{func.__name__} error] {ex}")
    return inner_function