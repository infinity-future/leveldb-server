
from leveldbs import LevelDBClient

c = LevelDBClient('localhost', 11300)

assert c.get(b'a') is None, "c.get(b'a') should be None as first"
assert c.get(b'a', 10) == 10, "c.get(b'a', 10) == 10"
c.put(b'a', b'b')
assert c.get(b'a') == b'b', "c.get(b'a') == b'b'"
c.delete(b'a')
assert c.get(b'a') is None, "c.get(b'a') should be None as first"
assert c.get(b'a', 10) == 10, "c.get(b'a', 10) == 10"

print('test done')
