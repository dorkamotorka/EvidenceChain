import tlsh 
import ssdeep
import pyLZJD

# two texts with the only difference being that the second text (t2) uses a capital B for the first occurence of the word "building"
t1 = "Because highly fit schemata of low defining length and low order play such an important role in the action of genetic algorithms, we have already given them a special name: building blocks. Just as a child creates magnificent fortresses through the arrangement of simple blocks of wood, so does a genetic algorithm seek near optimal performance through the juxtaposition of short, low-order, high-performance schemata, or building blocks"
t2 = "Because highly fit schemata of low defining length and low order play such an important role in the action of genetic algorithms, we have already given them a special name: Building blocks. Just as a child creates magnificent fortresses through the arrangement of simple blocks of wood, so does a genetic algorithm seek near optimal performance through the juxtaposition of short, low-order, high-performance schemata, or building blocks"

s1 = ssdeep.hash(t1)
s2 = ssdeep.hash(t2)

h1 = tlsh.hash(t1.encode())
h2 = tlsh.hash(t2.encode())

p1 = pyLZJD.digest(t1.encode())
p2 = pyLZJD.digest(t2.encode())

print("TEXT COMPARISON: ")

print("TLSH hash comparison(the lower the number, the better):")
print("difference = %d\n" % tlsh.diff(h1, h2))

print("SSDeep hash comparison(the higher the number the better):")
print("similarity = %d\n" % ssdeep.compare(s1, s2))

print("LZJD hash comparison(the higher the number the better):")
print("similarity = %d\n" % pyLZJD.sim(p1, p2))

print("============================================================")

with open("orig.jpg", "rb") as f:
	orig = f.read()

with open("fake.jpg", "rb") as f:
	fake = f.read()

with open("orig_onebytechanged.jpg", "rb") as f:
	orig_changed = f.read()

s1 = ssdeep.hash(orig)
s2 = ssdeep.hash(fake)

h1 = tlsh.hash(orig)
h2 = tlsh.hash(fake)
h3 = tlsh.hash(orig_changed)

p1 = pyLZJD.digest(orig)
p2 = pyLZJD.digest(fake)

print("IMAGE COMPARISON: ")
print("TLSH hash comparison(the lower the number, the better):")
print("difference = %d\n" % tlsh.diff(h1, h2))

print("SSDeep hash comparison(the higher the number the better):")
print("similarity = %d\n" % ssdeep.compare(s1, s2))

print("LZJD hash comparison(the higher the number the better):")
print("similarity = %d\n" % pyLZJD.sim(p1, p2))

print("============================================================")

print("ORIG vs ORIG WITH ONE CHANGED BYTE")
print("TLSH")
print(f"difference = {tlsh.diff(h1, h3)}")
