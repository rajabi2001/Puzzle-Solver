import io
import collections
from Cell import Cell

mypuzzle = []
mygraph = collections.defaultdict(list)


address = ".\puzzles\puzzle0.txt"
with open(address) as reader :
    myinput = reader.read()


buf = io.StringIO(myinput)
n , m = map(int ,buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" "))
for i in range(n):
    buffread = buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" ")
    mynd = []
    for ii in range(m) : 
        mynd.append(buffread[ii])
    mypuzzle.append(mynd)

for i in range(1,n+1):
    for ii in range(1,m+1):
        mygraph[(i,ii)].append(Cell())

