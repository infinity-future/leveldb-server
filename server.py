
import argparse
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import plyvel

class LevelDB:
    def __init__(self, data):
        self.db = plyvel.DB(data, create_if_missing=True)
    
    def put(self, k, v):
        return self.db.put(k, v)
    
    def get(self, k):
        return self.db.get(k)
    
    def delete(self, k):
        return self.db.delete(k)

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main(port, data):
    # Create server
    server = SimpleXMLRPCServer(
        ('0.0.0.0', port),
        requestHandler=RequestHandler,
        use_builtin_types=True,
        allow_none=True
    )
    server.register_introspection_functions()
    server.register_instance(LevelDB(data))

    # Run the server's main loop
    server.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LevelDB Server')
    parser.add_argument(
        '--port', type=int, default=11300,
        help='Port of server')
    parser.add_argument('--data', type=str, default='/leveldb',
        help='Path of database')
    args = parser.parse_args()
    main(args.port, args.data)
