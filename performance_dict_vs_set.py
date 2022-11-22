import time


class Stopwatch:
    # create and start a stop watch
    def __init__(self) -> None:
        self.__start_time: int = time.perf_counter_ns()

    def restart(self) -> None:
        self.__start_time = time.perf_counter_ns()

    # returns elapsed time since stopwatch was started
    def elapsed_time(self, resolution: int = 1e-9) -> int:
        """
        :param resolution: resolution down to ns; default 1e-9
        :return: elapsed time since stopwatch was started
        """
        elapsed = time.perf_counter_ns() - self.__start_time
        return elapsed * resolution


def dict_test(iterator):
    my_dict = dict()
    for i in iterator:
        if i not in my_dict:
            my_dict.update({i: ""})


def set_test(iterator):
    my_set = set()
    for i in iterator:
        if i not in my_set:
            my_set.add(i)


loops = 10_000_000
run_list = list()
iterator = [i for i in range(loops)]


############################################
start_time = Stopwatch()

dict_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"dic: {str(end_time)}")
############################################

############################################
start_time = Stopwatch()

set_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"set: {str(end_time)}")
############################################

############################################
start_time = Stopwatch()

dict_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"dic: {str(end_time)}")
############################################

############################################
start_time = Stopwatch()

set_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"set: {str(end_time)}")
############################################

############################################
start_time = Stopwatch()

dict_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"dic: {str(end_time)}")
############################################

############################################
start_time = Stopwatch()

set_test(iterator)

end_time = start_time.elapsed_time()
run_list.append(f"set: {str(end_time)}")
############################################




# ############################################
# start_time = Stopwatch()
#
# for i in range(100_000_000):
#     foo = None
#
# end_time = start_time.elapsed_time()
# run_list.append(f"None: {str(end_time)}")
# ############################################
#
# ############################################
# start_time = Stopwatch()
#
# for i in range(100_000_000):
#     foo = ""
#
# end_time = start_time.elapsed_time()
# run_list.append(f'"": {str(end_time)}')
# ############################################




print(str(run_list))
