import logging
import time


def use_logging(level):
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            beforeTs = int(round(before * 1000))
            result = func(*args, **kwargs)
            time.sleep(5)
            after = time.time()
            afterTs = int(round(after * 1000))
            message = 'time elapsed %r ms for running function %s: ' % (afterTs - beforeTs, func.__name__)
            if level == 'warn':
                logging.warn(message)
            else:
                logging.info(message)
            return result

        return wrapper

    return timer


@use_logging(level='warn')
def add(x, y=10):
    return x + y


print add(10)
