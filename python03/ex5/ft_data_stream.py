from typing import Generator
import time
#create an a function that create the events
def create_events(n : int) -> Generator[dict, None, None]:
    char = ["alice","bob","charlie"]
    actions = ["killed monster","found treasure","leveled up"]

    for i in range(n):
        yield {
            "event_id" : i + 1
            ,"name" : char[i % 3]
            ,"level" : (i % 20) + 1
            ,"action" : actions[i % 3]
        }
#create a function that stream those events
def process_event(n : int) ->None:
    start = time.time()
    total = 0
    High_level = 0
    Treasure_events = 0
    leveled_up = 0
    for event in create_events(n):
        if total < 3:
            print(f"Event {event['event_id']}: Player {event['name']} (level {event['level']}) {event['action']}")
        if event['level'] > 10:
            High_level = High_level + 1
        if event['action'] == "found treasure":
            Treasure_events += 1
        if event['action'] == "leveled up":
            leveled_up += 1
        total = total+1
    end = time.time()
    execs = end - start
    print("...")
    print("\n=== Stream Analytics ===")
    print("Total events processed:", total)
    print("High-level players (10+):", High_level)
    print("Treasure events:", Treasure_events)
    print("Level-up events:", leveled_up)
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {execs:.3f} seconds\n")

def Fibonacci() -> Generator[int,None,None]:
    a,b = 0,1
    while True:
        yield a
        a, b = b ,a + b
def primes() -> Generator[int, None, None]:
 n = 2
 while True:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        yield n
    n+=1

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")
    process_event(1000)

print("\n=== Generator Demonstration ===")

fib = Fibonacci()
fibostr = str(next(fib))
for i in range(9):
    fibostr = fibostr + ", " + str(next(fib))
print(f"Fibonacci sequence (first 10): {fibostr}")

prime = primes()
primstr = str(next(prime))
for p in range(4):
    primstr = primstr + ", " + str(next(prime))
print(f"Prime numbers (first 5): {primstr}")






        

        

