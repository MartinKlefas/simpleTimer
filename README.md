# Simple Timer
I just needed the world's simplest python code timer. Basically no learning curve and no features.

## Basic Operation
To start a timer for a block of code, instantiate your timer, then call `.start("name")`. when your code block is finished call `.stop("name")`:

    t = simpleTimer()
    t.start("my_time")
    ## SOME CODE
    t.stop("my_time")

## Looped Operation
If you've got code that you're going to repeat in a loop of any kind you can get an average time per loop with `start_looped()` and `stop_looped()`:
    t = simpleTimer()()
    for i in range(10):
        t.start_looped("timer1")
        ## SOME CODE
        t.stop_looped("timer1")

        t.start_looped("timer2")
        ## Some Other Code
        t.stop_looped("timer2")

## Using a "with" block
The last method of timing some code is to use a with block - which is basically just a style choice in this context, and implements the same basic start and stop functions automatically:

    with timer.start("my with task"):
        ## Some Code
        ## some more code

## Report generation
At the end of your code call `.report()` and it'll retirn a report to the string - so call `print(t.report()) ` if you want it printing to screen.