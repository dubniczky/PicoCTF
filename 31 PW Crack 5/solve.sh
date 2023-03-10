# Dump hex
cat level5.hash.bin | od -A n -t x1 | sed 's/ *//g'

# Search by hash
python pass.py | grep e8352e76e260a31eb266012f70df9a10

# Solve
echo "7e5f" | python level5.py