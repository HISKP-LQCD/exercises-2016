# Faster π with Monte Carlo in C with OpenMP

Some participants solved this quite quickly in R or Mathematica. Then I was
asked for ways to improve the program or algorithm. One first step is to use
all the cores/threads one has in the computer. If you are interested in such
technical things at this point, read on.

Parallelization of this problem is simple: Just let each of four threads
compute `N/4` of the points. Each thread locally counts the number of accepted
points. After the computation, the individual acceptance numbers are summed up
to give the total acceptance.

I have used C with OpenMP in this example. OpenMP makes simple things very
easy, things seem to get out of hand quickly. It also binds you to a compiler
with support for it; GCC is one of them. As you can see in the program, it gets
littered with `#pragma omp` directives which transform the C program in certain
ways. The core concepts of OpenMP are:

- The program does the right thing sequentially (not parallel) if one just ignores all the `#pragma omp` statements.

- Each `parallel` block creates a certain number of threads (can be controlled but defaults to the number of virtual cores). Tasks are then worked on in parallel (like a `for` loop), at the end the threads “join” and the program continues with a single thread. Variables that are defined within the `parallel` section are thread-local by default. The usage of the `reduction` will give each thread a copy of `accepted` and sum up the results at the end of the block.

Since OpenMP is not really part of the C language, it always seems a bit out of
place. Also you cannot reason about the constructs like you can with usual C.
Therefore I only use it for simple things.

This program does one billion iterations. Storing the intermediate results will
use at least 1 GB of RAM, computing a cumulative mean will quickly take up 4 GB
of RAM. Therefore I do not even attempt to retain them.

The `rand()` function, which has [a lot of
problems](https://www.youtube.com/watch?v=LDPMpc-ENqY) in its own right uses a
global variable and therefore you cannot use that in threads. The `rand_r` uses
an explicit pointer to a seed/state variable, this can then be used in threads.
I initialize those seeds with the thread ID. If two threads used the same seed,
their random numbers would be exactly the same and one does not gain any
precision in π.

Running it on my Core i5-2520M laptop, I get:

    $ bash compile.bash
    $ time ./pi
    π = 3.1415854360000001755
    29.45user 0.08system 0:07.73elapsed 381%CPU (0avgtext+0avgdata 1784maxresident)k
    0inputs+0outputs (0major+85minor)pagefaults 0swaps

It takes about 7.7 seconds and uses, on average 3.81 of the 4 threads that the
system supports. Whether this depends on Intel's HyperThreading, weaknesses in OpenMP or something else, I don't know. At least it is faster than the single threaded version:

    $ time env OMP_NUM_THREADS=1 ./pi
    π = 3.1415832359999997792
    14.61user 0.00system 0:14.61elapsed 99%CPU (0avgtext+0avgdata 1704maxresident)k
    0inputs+0outputs (0major+139minor)pagefaults 0swaps

You see that only 0.99 cores are used. The execution time has only doubled, the `user` time is halved! This means that the version with four threads already has a lot of overhead! Running it again with two threads gives the following:

    $ time env OMP_NUM_THREADS=2 ./pi
    π = 3.1415818519999998415
    15.39user 0.00system 0:07.72elapsed 199%CPU (0avgtext+0avgdata 1708maxresident)k
    0inputs+0outputs (0major+142minor)pagefaults 0swaps

Just the 7.7 seconds but 15 seconds of `user` time. So we can deduce from this
that the SMT (Intel calls it HyperThreading) does not really help anything, it
just creates overhead. See how the CPU usage is now at 1.99 cores which is very
nice. This might be because we only do simple operations (addition and
multiplication) here, those operations do not take many cycles; nothing else
can be run in parallel on the *same* core, really.

The results are also a bit different! This is because a each thread has a
different random seed. Therefore it is a difference whether one generator
creates all the numbers or two generators generate half of them each. The
difference is just statistical fluctuation but means that one cannot reproduce
the exact same result with a different number of threads.
