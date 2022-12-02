import asyncio, time
import inspect


async def main():
    print(f'{time.ctime()} Witaj!')
    result = await f()
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Żegnaj!')
    return result


def blocking():
    time.sleep(0.5)
    print(f'{time.ctime()} Witam z wątku')

async def f():
    await asyncio.sleep(1)
    return 123

# print(type(f))
# print(inspect.iscoroutinefunction(f))


# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
#
# loop.run_in_executor(None, blocking)
# loop.run_until_complete(task)
#
# pending = asyncio.all_tasks(loop=loop)
# for task in pending:
#     task.cancel()
# group = asyncio.gather(*pending, return_exceptions=True)
# loop.run_until_complete(group)
# loop.close()
