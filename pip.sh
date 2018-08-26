
rm -rf ./dist
cp version.txt ./leveldbs/
python3 setup.py sdist
twine upload dist/*.tar.gz
