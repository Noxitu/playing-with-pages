import random
import json
import sys

MEAN = 100.0
STDDEV = 15.0

def main():
    n = 100
    data = [random.gauss(MEAN, STDDEV) for _ in range(n)]
    mean = sum(data) / n
    stddev = (sum((x - mean) ** 2 for x in data) / n) ** .5
    
    with open('out.json', 'w') as fd:
        json.dump({'mean': mean, 'stddev': stddev}, fd)

    with open('data.json', 'w') as fd:
        json.dump(data, fd)

if __name__ == '__main__':
  main()
