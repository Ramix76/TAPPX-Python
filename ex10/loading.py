import time

# def ft_progress(lst):
#     start_time = time.time()
#     iter_time = 0
#     for i in lst:
#         if (i == 1):
#             iter_time = time.time() - start_time
#         print(
#             "\rETA: {:5.2f} [{:>4.0%}] [{:=>{}}{:{}}] {}/{} | elapsed time {:.2f}s"
#             .format(
#                 (len(lst) - i) * iter_time, i / len(lst),
#                 '',
#                 i * 25 / len(lst),
#                 '>',
#                 25 - i * 25 // len(lst),
#                 i + 1,
#                 len(lst),
#                 time.time() - start_time),
#             end="")
#         yield i


# def main():
#     listy = range(3333)
#     ret = 0
#     for elem in ft_progress(listy):
#         ret += elem
#         time.sleep(0.0008)
#     print()
#     print(ret)


# if __name__ == "__main__":
#     main()

def generator():

   yield "Welcome"

   yield "to"

   yield "Simplilearn"

gen_object = generator()

print(type(gen_object))

for i in gen_object:

   print(i)