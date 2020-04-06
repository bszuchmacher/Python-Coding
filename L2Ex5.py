# Question:
#
# -When would the use of generators be preferred
# over list comprehension and vice versa??

# Answer:

# 1) Iterating over the generator expression or the list comprehension
# will do the same thing. However, the list comprehension will
# create the entire list in memory first while the generator
# expression will create the items as it runs,
# so you are able to use it for very large (and also infinite!)
# sequences. TO SAVE MEMORY GENERATOR FUNCTION IS BETTER.

