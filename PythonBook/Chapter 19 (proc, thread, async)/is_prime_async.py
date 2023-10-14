import asyncio
import itertools
import math


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        try:
            await asyncio.sleep(.3)
        except asyncio.CancelledError:
            break
        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


async def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
        if i % 100_000 == 1:
            await asyncio.sleep(0)

    return True


async def main() -> bool:
    spinner = asyncio.create_task(spin("thinking"))
    result = await is_prime(5_000_111_000_222_021)
    spinner.cancel()
    print(f"\r{' ' * 10}\r", end="")
    return result

if __name__ == "__main__":
    print(asyncio.run(main()))
