import pydof

t4t = pydof.Parser()
config = pydof.Config()
config.read()
usage = t4t.get_usage(config.username(), config.password())
print usage.Volume.TotalUsage, usage.Volume.Limit
