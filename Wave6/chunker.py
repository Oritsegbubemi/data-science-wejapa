#If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), being able to take and use chunks of it at a time can be very valuable.

#Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

#Calling the function like this:

#for chunk in chunker(range(25), 4):
#    print(list(chunk))
#should output:

#[0, 1, 2, 3]
#[4, 5, 6, 7]
#[8, 9, 10, 11]
#[12, 13, 14, 15]
#[16, 17, 18, 19]
#[20, 21, 22, 23]
#[24]

def chunker(iterable,size):
    """yield successive chunks from iterable of length size"""
    for i in range(0,len(iterable),size):
        yield iterable[i:i + size]

for chunk in chunker(range(25),4):
    print(list(chunk))