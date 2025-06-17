#  _________________
#  Import LIBRARIES
import asyncio
#  Import  FILES
#  _________________


def main() -> None:
    print("Hello from master-asyncio-m!")


async def say_hello_async() -> None:
    await asyncio.sleep(delay=2)
    print("Hello, Async World!")


asyncio.run(main=say_hello_async())


if __name__ == "__main__":
    main()
