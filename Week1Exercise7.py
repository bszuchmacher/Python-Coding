def build_pyramid(height): #height of pyramid
    if (height > 0):
      for i in reversed(range(height)): #for each row in the height WE REVERSED IT... :)
          row = '*' * (1+2*i) #this is the pattern +1 star(2x row number)
          print(row.center(2 * height)) # print row centered 2x height
build_pyramid(7)
