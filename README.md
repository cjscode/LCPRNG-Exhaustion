This is a quick solution I wrote to solve the problem of identifying potential candidate parameters for a given m value to be used in a Linear Congruential Pseudo Random Number Generator. The script will ask you for an m value and then for you to define a search space. It checks all of the values for a and c by brute force/exhaustion within the search space. The script will return an array containing nested arrays comprised of suitable a, c value pairs.

Undoubtedly, this is a particularly inefficient algorithm for solving this problem but it does its job well for small search spaces. 
