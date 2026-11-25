import time
start = time.monotonic()
for i in range(100):
    i = i+1
end = time.monotonic()
taken = end - start
print("time taken is:", taken)    