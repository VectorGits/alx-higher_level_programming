#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv_int = [int(sys.argv[x]) for x in range(1, argc)]
    print(sum(argv_int))
    
    # Alternative solution for copycats :P
    # sum = 0
    # for x in range(1, argc):
    # 	sum += int(sys.argv[x])
    # print(sum)
