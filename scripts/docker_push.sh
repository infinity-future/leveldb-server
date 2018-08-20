sudo docker tag infinityfuture/leveldb-server:latest infinityfuture/leveldb-server:`cat version.txt` && \
    sudo docker push infinityfuture/leveldb-server:`cat version.txt` && \
    sudo docker push infinityfuture/leveldb-server:latest