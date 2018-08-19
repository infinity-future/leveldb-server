
sudo docker build --no-cache -t infinityfuture/leveldb-server:latest .
VERSION=`cat version.txt`
sudo docker tag infinityfuture/leveldb-server:latest infinityfuture/leveldb-server:$VERSION
sudo docker push infinityfuture/leveldb-server:latest
