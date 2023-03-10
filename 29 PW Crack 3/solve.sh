# Dump hex
cat level3.hash.bin | od -A n -t x1 | sed 's/ *//g'

# Search by hash
python pass.py | grep 03078179ea3e83075620b5ed18f95894

# Solve
echo "4b17" | python level3.py