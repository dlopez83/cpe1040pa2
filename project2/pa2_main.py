# Solution 1

# names = []

# def cap_join(names):

# 	names2 = " ".join(names).title()
# 	return names2

# if __name__ == '__main__':
# 	names = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]

# 	print(cap_join(names))

# Solution 2 

def cap_join(list1):

    names = []
    for index1 in list1:
        names.append(index1[0].upper() + index1[1:])
    return ' '.join(names)

if __name__ == '__main__':
	names2 = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]
	
	print(cap_join(names2))