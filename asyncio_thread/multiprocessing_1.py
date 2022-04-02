import multiprocessing
import time
# global value
#
# value = 0

# def plus_func(num):
#     value1 = 10
#     for i in range(num):
#         value1 += 1
#         print(value1)
#     time.sleep(0.5)
#
# def minus_func(num):
#     value2 =100
#     for i in range(num):
#         value2 -= 1
#         print(value2)
#     time.sleep(0.5)
#
#
#
# if __name__ == '__main__':
#     plus_process = multiprocessing.Process(target=plus_func, args=(10,))
#     minus_process = multiprocessing.Process(target=minus_func, kwargs={"num":10})
#     minus_process.start()
#     plus_process.start()
#
#     plus_process.join()
#     minus_process.join()


def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

if __name__ == '__main__':
    tic = time.time()

    process_list = []
    for i in range(10):
        p = multiprocessing.Process(target=sleepy_man)
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    toc = time.time()

    print('Done in {:.4f} seconds'.format(toc - tic))

