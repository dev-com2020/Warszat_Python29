import cProfile
from myapp import main

profiler = cProfile.Profile()
profiler.runcall(main)
profiler.print_stats()
