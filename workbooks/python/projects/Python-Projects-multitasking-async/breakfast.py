"""
Можете поиграться с задержками, чтобы увидеть, как меняется порядок выполнения
"""

from time import monotonic
import asyncio


async def make_tea():
    print('Boiling water...')
    await asyncio.sleep(.3)
    print('Putting tea in the cup')
    print('Pouring water into cup')
    print('Waiting for tea to steep...')
    await asyncio.sleep(.1)
    print('Tea is ready!')
    return '******************************tea', 'tea'


async def make_eggs():
    print('Warming the egg pan...')
    await asyncio.sleep(.3)
    print('cracking 2 eggs')
    print('cooking the eggs...')
    await asyncio.sleep(.2)
    print('Put eggs on plate')
    print('Eggs are ready!')
    return '******************************eggs', 'eggs'


async def make_toast():
    print('Putting a slice of bread in the toaster')
    print('Start toasting...')
    await asyncio.sleep(.3)
    print('Remove toast from toaster')
    print('Putting butter on the toast')
    print('Putting jam on the toast')
    print('Toast is ready!')
    return '******************************toast', 'toast'


async def make_breakfast():
    tasks = [make_tea(), make_eggs(), make_toast()]
    order = ['first', 'second', 'last']
    i = 0
    for task in asyncio.as_completed(tasks):
        result, result_type = await task
        if result_type == 'tea':
            print(f'****** I will drink tea {order[i]}')
        elif result_type == 'eggs':
            print(f'****** I will eat eggs {order[i]}')
        elif result_type == 'toast':
            print(f'****** I will eat toast {order[i]}')
        i += 1


if __name__ == '__main__':
    start_time = monotonic()
    asyncio.run(make_breakfast())
    finish_time = monotonic()
    print(f'Totally it took {(finish_time - start_time):.2f} min.')
