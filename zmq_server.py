
import pickle
import argparse
import threading
import zmq
import plyvel

PORT = 11300
THREADING_NUMBER = 5
DATA = '/leveldb'

class LevelDB:
    def __init__(self, data):
        self.db = plyvel.DB(data, create_if_missing=True)
    
    def put(self, k, v):
        return self.db.put(k, v)
    
    def get(self, k):
        return self.db.get(k)
    
    def delete(self, k):
        return self.db.delete(k)

def worker_routine(worker_url, database, context=None):
    """Worker routine"""
    context = context or zmq.Context.instance()
    # Socket to talk to dispatcher
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)
    while True:
        string = socket.recv()
        method, key, value = pickle.loads(string)
        print('Do', method, key[:20])
        try:
            if method == 'get':
                socket.send(pickle.dumps((None, database.get(key))))
            elif method == 'put':
                socket.send(pickle.dumps((None, database.put(key, value))))
            elif method == 'delete':
                socket.send(pickle.dumps((None, database.delete(key))))
            else:
                socket.send(pickle.dumps('Error: invalid method', None))
        except Exception as e:
            socket.send(pickle.dumps('Error: {}'.format(str(e)), None))


def main(port, data, threading_number):
    """Server routine"""

    database = LevelDB(data or DATA)

    url_worker = 'inproc://workers'
    url_client = 'tcp://*:{}'.format(port or PORT)
    # Prepare our context and sockets
    context = zmq.Context.instance()
    # Socket to talk to clients
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)
    # Socket to talk to workers
    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)
    # Launch pool of worker threads
    for _ in range(threading_number or THREADING_NUMBER):
        thread = threading.Thread(target=worker_routine, args=(url_worker, database))
        thread.start()
    zmq.proxy(clients, workers)
    # We never get here but clean up anyhow
    clients.close()
    workers.close()
    context.term()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LevelDB Server')
    parser.add_argument(
        '--port', type=int, default=11300,
        help='Port of server')
    parser.add_argument(
        '--threading-number', type=int, default=5,
        help='Threading number on server')
    parser.add_argument('--data', type=str, default='/leveldb',
        help='Path of database')
    args = parser.parse_args()
    main(args.port, args.data, args.threading_number)
