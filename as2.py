import asyncio
# import time
#
#
# def count():
#     print("one")
#     time.sleep(1)
#     print("two")
#
#
# def main():
#     for _ in range(3):
#         count()
#
#
# if __name__ == '__main__':
#
#
#     s = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - s
#     print(f'{__file__} executed in {elapsed:0.2f} sec')
def stuff():
    print("*******")

def py34_coro():
    yield from stuff()

async def py35_coro():
    await stuff()

py34_coro()
py35_coro()