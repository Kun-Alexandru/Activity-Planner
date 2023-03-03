import datetime

class exception(Exception):
    pass



def counter(a,b):
    if(a<b):
        pass
    else:
        raise exception("")


def fibo(n):
    memory = {0: 1, 1: 1}
    if n not in memory:
        memory[n] = fibo(n-1) + fibo(n-2)
    return memory[n]

# 0, 1, 1, 2, 3, 5, 8, 13, 21
if __name__ == '__main__':
    try:
        print("hehe")
        counter(30, 20)
    except exception as e:
        print("A>B")



#vect = [[datetime.time(00,00),datetime.time(14,00)],[datetime.time(17,30),datetime.time(23,59)],[datetime.time(15,30),datetime.time(16,00)]]

#date = datetime.date(1, 1, 1)
#freeTime = datetime.timedelta(seconds=0)
#for i in range (0, len(vect)):
#    datetime1 = datetime.datetime.combine(date, vect[i][0])
#    datetime2 = datetime.datetime.combine(date, vect[i][1])
#    freeTimeTime = datetime2 - datetime1
#    freeTime = freeTime + freeTimeTime

#print(freeTime)