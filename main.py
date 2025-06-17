#  _________________
#  Import LIBRARIES
import asyncio
#  Import  FILES
#  _________________


async def say_hello_async() -> None:
    await asyncio.sleep(delay=2)  # Simulates waiting for 2 seconds
    print("Done first task: Hello, Async World!")


async def do_something_else() -> None:
    print("Starting another task...")
    await asyncio.sleep(delay=1)  # Simulates doing something else for 1 second
    print("Finished another task!")


async def main() -> None:
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )


if __name__ == "__main__":
    asyncio.run(main=main())
