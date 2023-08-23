# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.
from random import random
import asyncio
import time

#coroutine to generate work
async def producer(queue):
    print(f' {time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio. sleep(value)
        # add to the queue
        await queue.put(value)
        print(f'{time.ctime()} Producer: put fvalue)')
    # send an all done signal
    await queue.put (None)
    print(f' {time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f' {time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got{item}')
# all done
print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio. Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    
# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:29:03 2023 Consumer: Done
#  Wed Aug 23 14:29:03 2023 Producer: Running
#  Wed Aug 23 14:29:03 2023 Consumer: Running
# Wed Aug 23 14:29:04 2023 Producer: put fvalue)
# Wed Aug 23 14:29:04 2023 >got0.7712937946316125
# Wed Aug 23 14:29:04 2023 Producer: put fvalue)
# Wed Aug 23 14:29:04 2023 >got0.12890625130125
# Wed Aug 23 14:29:05 2023 Producer: put fvalue)
# Wed Aug 23 14:29:05 2023 >got0.3620157001821185
# Wed Aug 23 14:29:06 2023 Producer: put fvalue)
# Wed Aug 23 14:29:06 2023 >got0.9194107855558312
# Wed Aug 23 14:29:06 2023 Producer: put fvalue)
# Wed Aug 23 14:29:06 2023 >got0.6778493270941052
# Wed Aug 23 14:29:07 2023 Producer: put fvalue)
# Wed Aug 23 14:29:07 2023 >got0.21752808649683852
# Wed Aug 23 14:29:07 2023 Producer: put fvalue)
# Wed Aug 23 14:29:07 2023 >got0.789475868893275
# Wed Aug 23 14:29:07 2023 Producer: put fvalue)
# Wed Aug 23 14:29:07 2023 >got0.035293297495580855
# Wed Aug 23 14:29:08 2023 Producer: put fvalue)
# Wed Aug 23 14:29:08 2023 >got0.5673533340527649
# Wed Aug 23 14:29:09 2023 Producer: put fvalue)
#  Wed Aug 23 14:29:09 2023 Producer: Done
# Wed Aug 23 14:29:09 2023 >got0.9937175794785744