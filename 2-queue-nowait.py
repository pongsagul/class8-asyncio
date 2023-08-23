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
        #print(f'{time.ctime()} Producer: put fvalue)')
    # send an all done signal
    await queue.put (None)
    print(f' {time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f' {time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer : got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
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

# Wed Aug 23 14:23:00 2023 Consumer: Done
# Wed Aug 23 14:23:00 2023 Producer: Running
# Wed Aug 23 14:23:00 2023 Consumer: Running
# Wed Aug 23 14:23:00 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:01 2023 >got0.036945741468746074
# Wed Aug 23 14:23:01 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:01 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:02 2023 >got0.9809376992161449
# Wed Aug 23 14:23:02 2023 >got0.4272259002915296
# Wed Aug 23 14:23:02 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:02 2023 >got0.08254465567205105
# Wed Aug 23 14:23:02 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:03 2023 >got0.6209669104584153
# Wed Aug 23 14:23:03 2023 >got0.08686510451697949
# Wed Aug 23 14:23:03 2023 >got0.12700798902601373
# Wed Aug 23 14:23:03 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:03 2023 Consumer : got nothing, waiting a while...
# Wed Aug 23 14:23:04 2023 >got0.7913121715496673
# Wed Aug 23 14:23:04 2023 Consumer : got nothing, waiting a while...
#  Wed Aug 23 14:23:04 2023 Producer: Done
# Wed Aug 23 14:23:04 2023 >got0.6184215133253318
# Wed Aug 23 14:23:04 2023 >got0.051534646841731924