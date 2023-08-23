from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep((id + 1)*0.1)
        # add to the queue 
        await queue.put(value)
        # print(f'{time.ctime()} Producer: put {value}') 
    # send an all done signal

    print(f'{time.ctime()} Producer {id}: Done') 

async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work 
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done 
        queue.task_done()
    # all done 
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine

async def main():
    # create a shared queue 
    queue = asyncio.Queue(2)
    # start consumer 
    _=asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # run the producer and consumer 
    await queue.join()


# start the asyncio program 
asyncio.run(main())

# Wed Aug 23 15:00:32 2023 Consumer: Running
# Wed Aug 23 15:00:32 2023 Producer: Running
# Wed Aug 23 15:00:32 2023 Producer: Running
# Wed Aug 23 15:00:32 2023 Producer: Running
# Wed Aug 23 15:00:32 2023 Producer: Running
# Wed Aug 23 15:00:32 2023 Producer: Running
# Wed Aug 23 15:00:32 2023 > got 0.3647445991210081
# Wed Aug 23 15:00:32 2023 > got 0.8575165738486457
# Wed Aug 23 15:00:33 2023 > got 0.5354540520696695
# Wed Aug 23 15:00:34 2023 > got 0.9548556404625613
# Wed Aug 23 15:00:35 2023 > got 0.6152666999256533
# Wed Aug 23 15:00:35 2023 > got 0.12476853513277042
# Wed Aug 23 15:00:36 2023 > got 0.7964211969645995
# Wed Aug 23 15:00:36 2023 > got 0.9694893163298913
# Wed Aug 23 15:00:37 2023 > got 0.5395059800018264
# Wed Aug 23 15:00:38 2023 > got 0.33399377267613195
# Wed Aug 23 15:00:38 2023 > got 0.8538717484972471
# Wed Aug 23 15:00:39 2023 > got 0.8872601949172519
# Wed Aug 23 15:00:40 2023 > got 0.5004298728046377
# Wed Aug 23 15:00:40 2023 > got 0.46972204500979187
# Wed Aug 23 15:00:41 2023 > got 0.7539710180208837
# Wed Aug 23 15:00:42 2023 > got 0.9970959314085358
# Wed Aug 23 15:00:43 2023 > got 0.3284956919904921
# Wed Aug 23 15:00:43 2023 > got 0.5534142674615765
# Wed Aug 23 15:00:44 2023 > got 0.2574154652096525
# Wed Aug 23 15:00:44 2023 > got 0.014371927689460273
# Wed Aug 23 15:00:44 2023 > got 0.8494340483851561
# Wed Aug 23 15:00:45 2023 > got 0.7298465047014584
# Wed Aug 23 15:00:46 2023 > got 0.8046808322053006
# Wed Aug 23 15:00:46 2023 > got 0.9336530553524685
# Wed Aug 23 15:00:47 2023 > got 0.8819505483372254
# Wed Aug 23 15:00:48 2023 > got 0.49204884404791505
# Wed Aug 23 15:00:49 2023 > got 0.7575489511058814
# Wed Aug 23 15:00:49 2023 > got 0.8242974175524086
# Wed Aug 23 15:00:50 2023 > got 0.3545666828493187
# Wed Aug 23 15:00:51 2023 > got 0.8539317949671605
# Wed Aug 23 15:00:51 2023 > got 0.22888704791326786
# Wed Aug 23 15:00:52 2023 > got 0.27370741304907187
# Wed Aug 23 15:00:52 2023 > got 0.10517261715434467
# Wed Aug 23 15:00:52 2023 > got 0.7978996347400654
# Wed Aug 23 15:00:53 2023 > got 0.1668305111767573
# Wed Aug 23 15:00:53 2023 > got 0.38935326321899255
# Wed Aug 23 15:00:53 2023 > got 0.7016321711261946
# Wed Aug 23 15:00:53 2023 Producer 0: Done
# Wed Aug 23 15:00:54 2023 > got 0.18112365469889158
# Wed Aug 23 15:00:54 2023 > got 0.11475027383351688
# Wed Aug 23 15:00:54 2023 > got 0.80203000190834
# Wed Aug 23 15:00:55 2023 > got 0.007503137203230481
# Wed Aug 23 15:00:55 2023 > got 0.6994010553101943
# Wed Aug 23 15:00:56 2023 > got 0.6944294467004886
# Wed Aug 23 15:00:56 2023 Producer 1: Done
# Wed Aug 23 15:00:57 2023 > got 0.35586718099798564
# Wed Aug 23 15:00:57 2023 > got 0.06197870372459757
# Wed Aug 23 15:00:57 2023 Producer 2: Done
# Wed Aug 23 15:00:57 2023 > got 0.45205076930318533
# Wed Aug 23 15:00:57 2023 Producer 3: Done
# Wed Aug 23 15:00:58 2023 > got 0.21511965675901124
# Wed Aug 23 15:00:58 2023 > got 0.32763991165359385
# Wed Aug 23 15:00:58 2023 Producer 4: Done
# Wed Aug 23 15:00:58 2023 > got 0.182752866631127
# Wed Aug 23 15:00:58 2023 > got 0.5499623105388112