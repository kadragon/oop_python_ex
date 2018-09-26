import datetime
import time
from functools import wraps


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer  # 2
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display_info('John', 25)
# 결과:
# display_info(John, 25) 함수가 실행됐습니다.
# display_info 함수가 실행된 총 시간: 1.0036139488220215 초
