# Функция aiter() возвращает асинхронный итератор для асинхронного итерирования по нему например в async for/in. 
# Эквивалентно вызову x.__aiter__().
# 1. Синтаксис:
#   aiter(async_iterable)
# 2. Параметры:
#   async_iterable - объект, который можно использовать в инструкции async for/in. 
#   Должен возвращать асинхронный итератор из своего метода __aiter__().
# 3. Возвращаемое значение:
# асинхронный итератор. 
# Объект, реализующий метод __anext__(), который возвращает awaitable объект, используемый совместно с инструкцией await.
aiter() , iter()
# В отличие от синхронной функции iter(), у aiter() нет варианта с двумя аргументами.