'''
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1
 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1
 1 1 0 0 0 1 1 1 1 0 0 0 1 1 0 0 0 0 0 1
 1 1 1 1 1 1 1 1 1 0 0 0 1 1 0 0 0 0 0 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1
 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1
 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1
 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Please write a function that detects rectangles made by the '0' characters in
this field.  Please describe approach.
Each rectangle should be expressed in the form:
Rectangle at x=2     y=1     width=3     height=3
Please note that (for this exercise) rectangles are not allowed to touch or intersect.

A rectangle is a grouping of '0' surrounded by '1's. That is, the data above contains ONLY
four rectangles. For a single '0' to be considered a rectangle, it would have to be
surrounded by '1's (not one of the cases in this example). Also, note that an area of '0'
cannot contain any grouping of '1's because that would imply that rectangles are intersecting/touching.
'''

'''
I think I could do an array of arrays with each representing a row in data. Then Probably have a pointer that goes through each at the same time and notes it. The first 0 you see would be the top left corner of
the rectangle every time, and the last 0 you see would be the top right.

The numbers I need are the row when you first see a 0 (y) and the column where you first see a 0 (x), then how wide the rectangle is and how tall it is. I am probably not going to make rectangles classes because that sounds annoying. Eh maybe I will why not. If you know top right and top left corner you get the width, if you know bottom left and top left corner you get height
'''

data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]        
    
def get_rectangles(data):
    rectangles = []
    visited = set()
    
    zeros = []

    # get arrays into zeros
    for y, array in enumerate(data):
        for x, value in enumerate(array):
            if value == 0:   
                zeros.append((x, y))
    print(zeros)

    for x, y in zeros:
        if (x, y) in visited:
            continue
        
        width, height = 0, 0
        # while the x keeps increasing and why stays the same
        while (x + width, y) in zeros:
            width += 1
            
        # we just need leftmost point of each row
        while (x, y + height) in zeros:
            height += 1
        
        # mark all points in rec that is being added as visited.
        # loops only go to the part thats necessary
        for i in range(y, y + height):
            for j in range(x, x + width):
                visited.add((j, i))
        
        rectangles.append((x, y, width, height))
        
    for x, y, width, height in rectangles:
        print(f"Rectangle at x={x}, y={y}, width={width}, height={height}")

get_rectangles(data)

print(get_rectangles(data))
