
from leveldbs import LevelDBClient

c = LevelDBClient('localhost', 11300)

c.put(b'a', b'b')
print(c.get(b'a'))
c.delete(b'a')
print(c.get(b'a'))

