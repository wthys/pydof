import pydof
import sys

t4t = pydof.Parser()
usage = t4t.get_usage(sys.argv[1],sys.argv[2])
print usage.Volume.TotalUsage, usage.Volume.Limit
