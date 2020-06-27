# Solution by Darrow Hartman -> https://github.com/Darrow8/EulerProject
# link to problem -> https://projecteuler.net/problem=721
# Problem 721
# Given is the function f(a,n)=⌊(⌈a−−√⌉+a−−√)n⌋.
# ⌊.⌋ denotes the floor function and ⌈.⌉ denotes the ceiling function.
# f(5,2)=27 and f(5,5)=3935.
#
# G(n)=∑a=1nf(a,a2).
# G(1000) mod 999999937=163861845.
# Find G(5000000). Give your answer modulo 999999937.


from math import *
import numpy
import decimal


# Create the f() function and convert the math to python
# f(a,n)=⌊(⌈a−−√⌉+a−−√)n⌋
def f(a,n):
    result = ceil(sqrt(a)) + sqrt(a)
    result = floor(numpy.power(result,n))
    return result

# examples from problem:
print(f(5,2))  # should equal 27
print(f(5,5))  # should equal 3935


# Create the g() function and convert the math to python
# G(n)=∑a=1nf(a,a2).
def orginal_g(n):
    final_result = 0

    for a in range(1,n):
        final_result += f(a,numpy.power(a,2))

    return final_result

# examples from problem: (Cannot run)
# print(orginal_g(1000) % 999999937)  # will return error "OverflowError: (34, 'Result too large')"

# The problem with running this code and solving the answer is that these numbers are too large.
# g(1000) is an astronomically large number, which python will throw an overflow error for.
# Instead of trying to compute it AND THEN doing mod 999999937, if we incorporate the mod with
# the g(1000) then we *fingers crossed* won't get screwed.
# Furthermore, we can't even do f(1000,1000**2), the last call to the function, because even that returns in an error!
# So instead we must figure out a way to "parse" the result *as* it is being calculated by f()

# print(f(1000,1000**2)) # will result in error

# I think that this is because when performing (ceil(sqrt(a)) + sqrt(a)), we actually get a pretty big decimal.
# This adds a ton of computational work for the program. So I am going to cap the decimal at 10 places.


# in this new function, 'm' is the mod value we want to use
def good_g(n,m):
    # decimal.getcontext().prec = 10000
    final_result = (0)
    for a in range(1,n):

        print('"a" value of: ' + str(a))

        # directly imported f() code so that we could try to avoid an overflow

        original_result = round(ceil(sqrt(a)) + sqrt(a),5)
        print(original_result)
        # split ^2 function into two parts
        current_result = floor((original_result**(original_result))) # this is the sqrt(original_result) version of the full!


        # square it to add back the other part
        current_result = current_result **original_result

        #     If it is bigger than m, do the modulo
        if (current_result > m):
            result = decimal.Decimal(current_result % m)

        final_result += decimal.Decimal(current_result)


        print('adding result is: ' + "{:e}".format(decimal.Decimal(final_result)))



        print('full result is: ' + "{:e}".format(decimal.Decimal(final_result)))

    return str('final result is: ' + "{:e}".format(final_result))


print(good_g(1000,999999937))
