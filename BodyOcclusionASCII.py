print("Welcome to the ASCII Art Generator!")

size = int(input("Enter a value for the size of the person:\n"))
box_width = int(input("Box width:\n"))
box_height = int(input("Box height:\n"))

print("\nHere is the drawing:\n")

# Strings that will be used for drawing the scene
head = "   o "
body = "  ooo"
legs = "  o o"
box = "x"

head_list = []
body_list = []
legs_list = []

for i in head:
    head_list.append(i)
for i in body:
    body_list.append(i)
for i in legs:
    legs_list.append(i)

if box_height > 2 * size + 1 or size == 0:  # Box height is greater than the height of the person
    for i in range(box_height):
        for j in range(box_width):
            print(box, end="")
        print()

else:  # Box height is less than or equal to the height of the person

    # Code block for printing the head of the person
    if box_height > 2 * size:  # Head will be fully occluded
        for i in range(box_width):
            print(box, end="")
        occluded_head = ""
        for i in head_list[box_width:]:
            occluded_head = occluded_head + i
        print(occluded_head)
    else:  # No occlusion of the head
        print(head)

    # Code block for printing the body
    if box_height >= 2 * size:  # Full occlusion of the body
        for i in range(size):
            for j in range(box_width):
                print(box, end="")
            occluded_body = ""
            for j in body_list[box_width:]:
                occluded_body = occluded_body + j
            print(occluded_body)
    elif 2 * size >= box_height > size:  # Partial occlusion of the body
        for i in range(2 * size - box_height):
            print(body)
        for i in range(box_height - size):
            for j in range(box_width):
                print(box, end="")
            occluded_body = ""
            for j in body_list[box_width:]:
                occluded_body = occluded_body + j
            print(occluded_body)
    else:  # No occlusion
        for i in range(size):
            print(body)

    # Code block for printing the legs
    if box_height >= size:  # Full occlusion of the legs
        for i in range(size):
            for j in range(box_width):
                print(box, end="")
            occluded_legs = ""
            for j in legs_list[box_width:]:
                occluded_legs = occluded_legs + j
            print(occluded_legs)
    elif box_height < size:  # Partial occlusion or no occlusion
        for i in range(size - box_height):
            print(legs)
        for i in range(box_height):
            for j in range(box_width):
                print(box, end="")
            occluded_legs = ""
            for j in legs_list[box_width:]:
                occluded_legs = occluded_legs + j
            print(occluded_legs)
