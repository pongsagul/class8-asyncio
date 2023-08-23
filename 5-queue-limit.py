from random import random
import asyncio
import time

# coroutine to generate work
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

# coroutie to consume work
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
        # mark as completed
        queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:45:52 2023 Consumer: Running
# Wed Aug 23 14:45:52 2023 Producer: Running
# Wed Aug 23 14:45:52 2023 Producer: Running
# Wed Aug 23 14:45:52 2023 Producer: Running
# Wed Aug 23 14:45:52 2023 Producer: Running
# Wed Aug 23 14:45:52 2023 Producer: Running
# Wed Aug 23 14:45:52 2023 >got 0.34086045441885404
# Wed Aug 23 14:45:52 2023 >got 0.3444823561956246
# Wed Aug 23 14:45:53 2023 >got 0.48437055474266333
# Wed Aug 23 14:45:53 2023 >got 0.13782890077599763
# Wed Aug 23 14:45:53 2023 >got 0.5006088980102843
# Wed Aug 23 14:45:54 2023 >got 0.16921577745808303
# Wed Aug 23 14:45:54 2023 >got 0.655081765321239
# Wed Aug 23 14:45:55 2023 >got 0.22639844105733786
# Wed Aug 23 14:45:55 2023 >got 0.18414232633069372
# Wed Aug 23 14:45:55 2023 >got 0.14166303416175496
# Wed Aug 23 14:45:55 2023 >got 0.07836468866941959
# Wed Aug 23 14:45:55 2023 >got 0.6282910530746869
# Wed Aug 23 14:45:56 2023 >got 0.8015647947953047
# Wed Aug 23 14:45:57 2023 >got 0.2490846006946239
# Wed Aug 23 14:45:57 2023 >got 0.3463632582045577
# Wed Aug 23 14:45:57 2023 >got 0.24263270624874111
# Wed Aug 23 14:45:58 2023 >got 0.5622676096416503
# Wed Aug 23 14:45:58 2023 >got 0.7782617050578792
# Wed Aug 23 14:45:59 2023 >got 0.6849658040756984
# Wed Aug 23 14:46:00 2023 >got 0.86443252065654
# Wed Aug 23 14:46:01 2023 >got 0.25317028620316817
# Wed Aug 23 14:46:01 2023 >got 0.7948106934040117
# Wed Aug 23 14:46:02 2023 >got 0.7627822882590859
# Wed Aug 23 14:46:02 2023 >got 0.7877952490920966
# Wed Aug 23 14:46:03 2023 >got 0.7542612632493831
# Wed Aug 23 14:46:04 2023 >got 0.9114273965489023
# Wed Aug 23 14:46:05 2023 >got 0.2541856874236311
# Wed Aug 23 14:46:05 2023 >got 0.310217899929651
# Wed Aug 23 14:46:05 2023 >got 0.4152803226451013
# Wed Aug 23 14:46:06 2023 >got 0.6193780420289929
# Wed Aug 23 14:46:06 2023 >got 0.4917445952173808
# Wed Aug 23 14:46:07 2023 >got 0.9624543752975254
# Wed Aug 23 14:46:08 2023 >got 0.86727264391484
# Wed Aug 23 14:46:09 2023 >got 0.24832328019186367
# Wed Aug 23 14:46:09 2023 >got 0.7370542281132771
# Wed Aug 23 14:46:10 2023 >got 0.8894161901453083
# Wed Aug 23 14:46:11 2023 >got 0.7814380087782917
# Wed Aug 23 14:46:12 2023 >got 0.610674964085092
# Wed Aug 23 14:46:12 2023 Producer: Done
# Wed Aug 23 14:46:12 2023 >got 0.7117707302725946
# Wed Aug 23 14:46:13 2023 >got 0.06862787876531906
# Wed Aug 23 14:46:13 2023 >got 0.46005681738279003
# Wed Aug 23 14:46:13 2023 >got 0.9270258345227482
# Wed Aug 23 14:46:14 2023 >got 0.31540594495842744
# Wed Aug 23 14:46:15 2023 >got 0.9508413697572446
# Wed Aug 23 14:46:16 2023 >got 0.3817607310907646
# Wed Aug 23 14:46:16 2023 Producer: Done
# Wed Aug 23 14:46:16 2023 >got 0.4517519886742042
# Wed Aug 23 14:46:16 2023 Producer: Done
# Wed Aug 23 14:46:16 2023 >got 0.58005569587535
# Wed Aug 23 14:46:16 2023 Producer: Done
# Wed Aug 23 14:46:17 2023 >got 0.9907175322358255
# Wed Aug 23 14:46:17 2023 Producer: Done
# Wed Aug 23 14:46:18 2023 >got 0.542735070054182
# Wed Aug 23 14:46:19 2023 >got 0.7148783497585227