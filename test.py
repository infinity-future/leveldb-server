
from client import LevelDBClient

c = LevelDBClient('http://localhost:11300')


c.put(b'a', b'b')
print(c.get(b'a'))
c.delete(b'a')
print(c.get(b'a'))

