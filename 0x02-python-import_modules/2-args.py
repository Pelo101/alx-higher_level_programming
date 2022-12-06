#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    print("{} arguments:".format(count))
for elements in sys.argv:
    count += 1
print('{}:{}'.format(sys.argv.index(elements), elements))
