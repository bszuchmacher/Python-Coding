def build_pyramid(height): #height of pyramid
    if (height > 0):
      for i in range(height): #for each row in the height
          row = '*' * (2 * i + 1) #this is the pattern 2x row number +1 stars
          print(row.center(2 * height)) # print row centered 2x height
build_pyramid(7)
