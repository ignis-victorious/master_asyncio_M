


#  _________________
#  Import LIBRARIES
import asyncio
#  Import  FILES
#  _________________

def main():
    print("Hello from master-asyncio-m!")


async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async World!")

asyncio.run(say_hello_async())


if __name__ == "__main__":
    main()
