from random import random
import asyncio
import time

#coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate a value
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
    print(f'{time.ctime()} Producer: Done')

#coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # retrieve the get() awaitable
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item :
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

#entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

#start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:40:34 2023 Consumer: Running
# Wed Aug 23 14:40:34 2023 Producer: Running
# Wed Aug 23 14:40:34 2023 >got 0.3771755991157484
# Wed Aug 23 14:40:35 2023 >got 0.2692944597787238
# Wed Aug 23 14:40:35 2023 >got 0.016418341715568996
# Wed Aug 23 14:40:35 2023 >got 0.15724426701974625
# Wed Aug 23 14:40:36 2023 >got 0.9361732060828395
# Wed Aug 23 14:40:37 2023 >got 0.5178074149601285
# Wed Aug 23 14:40:37 2023 >got 0.43653217465257066
# Wed Aug 23 14:40:38 2023 >got 0.9936542649110299
# Wed Aug 23 14:40:39 2023 >got 0.40156167458971503
# Wed Aug 23 14:40:39 2023 Producer: Done
# Wed Aug 23 14:40:39 2023 >got 0.6447914993423102