from factordb.factordb import FactorDB
import gmpy2


n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423


f = FactorDB(n)
f.connect()

p, q = f.get_factor_list()

ph = (p-1)*(q-1)
d = gmpy2.invert(e, ph)
message = pow(c, d, n)

print(f"{bytearray.fromhex(format(message, 'x')).decode()}")