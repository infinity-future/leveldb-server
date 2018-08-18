import xmlrpc.client

s = xmlrpc.client.ServerProxy(
    'http://localhost:11300', use_builtin_types=True,
    allow_none=True
)

s.put(b'a', b'b')
print(s.get(b'a'))

# Print list of available methods

