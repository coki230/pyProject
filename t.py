import time

start = time.time_ns() / 1000000
print(start)
time.sleep(1)
end = time.time_ns() / 1000000
print(end - start)

