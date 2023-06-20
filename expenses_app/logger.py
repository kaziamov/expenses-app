import logging
import structlog


logging.basicConfig(
    level=logging.INFO, format="%(levelname)s:     %(asctime)s - %(message)s"
)

logger = logging.getLogger("expenses_app")


def log_this_input_and_output(func):
    async def inner(*args, **kwargs):
        logger.info("[{}.{}] input: {}, {}".format(
            (func.__module__),
            (func.__name__),
            "".join(*args),
            kwargs
        ))
        result = await func(*args, **kwargs)
        logger.info("[{}.{}] output: {}".format(
            (func.__module__),
            (func.__name__),
            result
        ))
        return result
    return inner


def log_this_output(func):
    async def inner(*args, **kwargs):
        result = await func(*args, **kwargs)
        logger.info("[{}.{}] output: {}".format(
            (func.__module__),
            (func.__name__),
            result
        ))
        return result
    return inner
