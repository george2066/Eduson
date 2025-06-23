"""
Более сложный пример для понимания, где идет переключение между задачами.
Обратите внимание, что всегда доходим до I/O операции. Ключевое слово await само по себе не отпускает.
"""

import asyncio


async def first_program():
    print('Program 1: awaiting sleep')
    await asyncio.sleep(1.1)
    print('Program 1: after sleep, sleeping again')
    await asyncio.sleep(1)
    print('Program 1: done')


async def program_task(program_name):
    print(f'Program {program_name} task: awaiting sleep')
    await asyncio.sleep(1)
    print(f'Program {program_name} task: after sleep, sleeping again')
    await asyncio.sleep(1)
    print(f'Program {program_name} task: done')


async def second_program():
    print('Program 2: creating task')
    task = asyncio.create_task(program_task('2'))
    print('Program 2: awaiting sleep')
    await asyncio.sleep(1)
    print('Program 2: after sleep, awaiting task')
    await task
    print('Program 2: done')


async def third_program():
    print('Program 3: starting task with timeout')
    await asyncio.sleep(0)
    try:
        async with asyncio.timeout(0.5):
            await program_task('3')
    except asyncio.TimeoutError:
        print('Program 3: task timed out')
    print('Program 3: awaiting sleep')
    await asyncio.sleep(1)
    print('Program 3: done')


async def main():
    print('Starting main')
    await asyncio.gather(first_program(), second_program(), third_program())
    print('Done')


if __name__ == '__main__':
    asyncio.run(main())
