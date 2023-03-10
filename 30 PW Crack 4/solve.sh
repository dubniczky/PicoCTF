# Dump hex
cat level4.hash.bin | od -A n -t x1 | sed 's/ *//g'

# Search by hash
python pass.py | grep 21153e2fab120c22f7e3a5df6a4c2c48

# Solve
echo "eacc" | python level4.py