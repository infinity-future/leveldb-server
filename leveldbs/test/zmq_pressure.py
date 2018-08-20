
import time
import uuid
import numpy as np
from leveldbs import LevelDBClient

c = LevelDBClient('localhost', 11300)
times = 10
unit = 1024 * 1024 // 8 # 1MB
mul = 100

prefix = str(uuid.uuid4())
sync = False

start_time = time.time()
for k in range(times):
    v = np.random.random(unit * mul) # mul MB
    k = '{}_{}'.format(prefix, k)
    c.put(k, v, sync=sync)
end_time = time.time()
spend = end_time - start_time
print('put time', spend, times * mul / spend)

start_time = time.time()
for k in range(times):
    k = '{}_{}'.format(prefix, k)
    v = c.get(k, sync=sync)
end_time = time.time()
spend = end_time - start_time
print('get time', spend, times * mul / spend)

start_time = time.time()
for k in range(times):
    k = '{}_{}'.format(prefix, k)
    v = c.delete(k, sync=sync)
end_time = time.time()
spend = end_time - start_time
print('delete time', spend, times * mul / spend)
