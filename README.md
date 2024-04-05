# Simple Timer
I just needed the world's simplest python code timer. Basically no learning curve and no features.

## Basic Operation
To start a timer for a block of code, instantiate your timer, then call `.start("name")`. when your code block is finished call `.stop("name")`:

    t = simpleTimer.Timer()
    t.start("my_time")
    ## SOME CODE
    t.stop("my_time")

## Looped Operation
If you've got code that you're going to repeat in a loop of any kind you can get an average time per loop with `start_looped()` and `stop_looped()`:

    t = simpleTimer.Timer()
    for i in range(10):
        t.start_looped("timer1")
        ## SOME CODE
        t.stop_looped("timer1")

        t.start_looped("timer2")
        ## Some Other Code
        t.stop_looped("timer2")

## Using a "with" block
The last method of timing some code is to use a with block - which is basically just a style choice in this context, and implements the same basic start and stop functions automatically:

    t = simpleTimer.Timer()
    with t.start("my with task"):
        ## Some Code
        ## some more code

## Report generation
At the end of your code call `.report()` and it'll return a report to the string - so call `print(t.report()) ` if you want it printing to screen. In the end you'll have something like the below:

    import time
    from simpleTimer import Timer
    t = Timer()
    t.start("first_task")
    time.sleep(1)
    t.stop("first_task")
    
    for i in range(10): 
        t.start_looped("looped_task")
        time.sleep(.2)
        t.stop_looped("looped_task")
    print(t.report())

        Elapsed time for first_task: 1.0013642311096191 seconds
        There were 10 repeats of looped_task, average duration was: 0.20438737869262696 seconds

