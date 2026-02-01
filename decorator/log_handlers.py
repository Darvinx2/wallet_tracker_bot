import functools


def log_callback(logger):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            event = None
            for arg in args:
                if hasattr(arg, "from_user"):
                    event = arg
                    break

            if event is None:
                return await func(*args, **kwargs)

            user_id = event.from_user.id

            if hasattr(event, "data"):
                logger.info(f"User {user_id} pressed button with data {event.data}")

            if hasattr(event, "text"):
                logger.info(f"User {user_id} pressed button with data {event.text}")

            return await func(*args, **kwargs)

        return wrapper

    return decorator
