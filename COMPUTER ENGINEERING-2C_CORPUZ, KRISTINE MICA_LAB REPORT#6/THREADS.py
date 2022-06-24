from time import sleep, perf_counter

def task():
    print('Finding something to do...')
    sleep(1)
    print('none')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
