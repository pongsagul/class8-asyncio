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
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

#coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            # retrieve the get() awaitable
            get_await = queue.get()
            # await the awaitable with a time out
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waitting...')
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

#entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

#start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:29:27 2023 Producer: Running
# Wed Aug 23 14:29:27 2023 Consumer: Running
# Wed Aug 23 14:29:27 2023 >got 0.394474823774807
# Wed Aug 23 14:29:28 2023 Consumer: gave up waitting...
# Wed Aug 23 14:29:28 2023 >got 0.7335958493632717
# Wed Aug 23 14:29:28 2023 Consumer: gave up waitting...
# Wed Aug 23 14:29:29 2023 Consumer: gave up waitting...
# Wed Aug 23 14:29:29 2023 >got 0.9960153238502385
# Wed Aug 23 14:29:29 2023 >got 0.10004371867083128
# Wed Aug 23 14:29:30 2023 Consumer: gave up waitting...
# Wed Aug 23 14:29:30 2023 >got 0.8013611743980333
# Wed Aug 23 14:29:30 2023 >got 0.009231839396849462
# Wed Aug 23 14:29:30 2023 >got 0.12361068547606102
# Wed Aug 23 14:29:30 2023 >got 0.11291974784411807
# Wed Aug 23 14:29:30 2023 >got 0.05844224392191555
# Wed Aug 23 14:29:30 2023 Producer: Done
# Wed Aug 23 14:29:30 2023 >got 0.19586258774848164
# Wed Aug 23 14:29:30 2023 Consumer: Done