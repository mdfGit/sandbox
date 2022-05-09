import asyncio
from string import ascii_uppercase

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print ('done fetching')
    return {'data': "beep beep"}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def really_cant_wait(trace):
    print(f'I really cannot wait! {trace}')

async def main():
    task1 = asyncio.create_task(print_numbers())
    task3 = asyncio.create_task(really_cant_wait("defined BEFORE await"))
    # This will take 2 seconds
    # await says, pause here and come back to the parent method when fetch_data is ready
    data = await fetch_data()
    print(f'data returned, awaited {data}')
    # why doesn't really can't wait run during the fetch_data await period?
    # because it is defined AFTER the await - it is not processed as an instruction
    task2 = asyncio.create_task(really_cant_wait("defined AFTER await"))
    # this will not run since await above is... waiting.
    print('Why am I waiting? Because my parent method has an await')
    
    # Note: if you want to wait until the counter ends to end the program
    # then use: "await task1" here.  
    # Otherwise, if you use no more awaits or a task that ends faster  
    # .e.g. "await task3", then the whole main() program ends without waiting on the counter (task1) 
    await task1

    print('end')

asyncio.run(main())