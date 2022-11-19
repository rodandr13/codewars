"""
Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd
parameter.

Python, Javascript, Java, Ruby versions: return results in a list/array

NOTICE:

Do NOT worry about checking zeros or negative values.
To find out if 3rd parameter (the upper limit) is inclusive or not, check
the tests, it differs in each translation
"""


def multiples(s1,s2,s3):
    return list(filter(lambda x: not x % s1 and not x % s2, range(1, s3)))
