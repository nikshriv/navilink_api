import asyncio
import json
from navien_api import NavilinkConnect

async def start():
    userId = input("Enter email: ")
    password = input("Enter password: ")
    navien = NavilinkConnect(userId=userId,passwd=password)
    await navien.start()
    for channel in navien.channels.values():
        print("\nChannel Info: ")
        print(channel.channel_info)
    for i in range(0,4):
        for channel in navien.channels.values():
            wait_time = 0.0
            while not len(channel.channel_status) and wait_time < 15:
                await asyncio.sleep(0.5)
                wait_time += 0.1
            print("\nChannel Status: ")
            print(channel.channel_status)
            await asyncio.sleep(15)
    await navien.disconnect()
    await asyncio.sleep(1)

asyncio.run(start())