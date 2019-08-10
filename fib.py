import sys

class Fib:
    def __init__(self):
        self.fib1t = 0#---------------------------tallies for keeping track of how many
        self.fib2t = 0#---------------------------times each function type is called

    def fib1(self, last, a=0, b=1, arr=[]):#------recursive version
        if last <= 0:                       
            return 'Enter a value greater than 0'
        temp = a
        arr.append(a)
        if last > 1:
            try:
                return self.fib1(last-1, a=a+b, b=a, arr=arr)
            except:
                err = '\n\nError: ' + str(sys.exc_info()[1]) + '\n' #likely to experience maximum
                return [err, 'err']                                 #recursion depth error
        self.fib1t += 1
        return arr

    def fib2(self, last):#------------------------for-loop version
        if last <= 0:
            return 'Enter a value greater than 0'
        arr = []
        a = 0
        b = 1
        for n in range(1, last+1):
            arr.append(a)
            temp = a
            a = a + b
            b = temp
        self.fib2t += 1
        return arr
    
    def check_tally(self, num):#------------------for checking tallies
        if num == 1 or num == 2:
            fib = 'fib1' if num == 1 else 'fib2'
            tally = str(self.fib1t) if num == 1 else str(self.fib2t)
            print(fib + ' has been run ' + \
            tally + ' time' + \
            ('.\n' if tally == '1' else 's.\n'))
        else:
            print('\nOnly 1 and 2 are valid arguments.\n')

def get_fun():#-----------------------------------getting user input to determine
    while True:#----------------------------------which function version to call
        fun = input('\nSelect a function [1, 2]: ')
        if fun != '1' and fun != '2':
            continue
        else:
            return int(fun)
    
def get_last():#----------------------------------getting user input to determine
    while True:#----------------------------------which fibonacci index to calculate
        last = input('Select a fibonacci index: ')
        try:
            last = int(last)
            if last > 0:
                return last
        except:
            continue

def print_result(fun, last, myFib):#--------------formatting print statement for final result
    result = myFib.fib1(last) if fun == 1 \
    else myFib.fib2(last)
    if result[-1] == 'err':
        return print(result[0])
    print('\n\nIndex ' + str(last) + ' of the Fibonacci sequence is ' + str(result[-1]) + '.\n')
    [myFib.check_tally(n) for n in range(1, 3)]

def main():#--------------------------------------MAIN LOOP
    myFib = Fib()#--------------------------------instantiating class in prep for main loop
    while True:
        fun = get_fun()
        last = get_last()
        print_result(fun, last, myFib)

main()


