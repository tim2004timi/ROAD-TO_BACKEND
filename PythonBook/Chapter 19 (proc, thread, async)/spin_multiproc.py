import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(.3):
            break
        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


def slow() -> int:
    time.sleep(60)
    return 100


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking! ", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f"\r{' ' * 10}\r", end="")
    print(f"answer: {result}")


if __name__ == "__main__":
    main()
