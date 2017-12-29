#!/usr/bin/env python3
import matplotlib.pyplot as plt

if __name__ == "__main__":
    numbers = [1,22,33,5,44] # Save your samples here
    plt.bar(range(len(numbers)), numbers, 0.35)
    plt.ylabel("selected word")
    plt.xlabel("occurrence over all chapters")
    plt.show()
