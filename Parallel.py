import multiprocessing as mp

print("Number of my computer processors: ", mp.cpu_count())
pool = mp.Pool(mp.cpu_count())
print(pool)

