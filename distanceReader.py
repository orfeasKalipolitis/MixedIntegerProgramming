
# Set the name of the file to be read
fileName = 'distances.dst'
distFile = open(fileName, 'r')

n = int(distFile.readline())

labels = []

# Get the name of the cities
cities = range(0, n)
for city in cities:
    labels.append(distFile.readline())

distances = []

# Get all the different distances on a matrix
for city in cities:
    distances.append([float(i) for i in distFile.readline().split()])

output_file = open("distancesForMathprog.txt", "w")

# print out city numbers and distances for mathprog
for fromCity in cities:
    lineStart = '    ' + str(fromCity + 1)

    for toCity in cities:
        # fix for 0-indexing

        if distances[fromCity][toCity] != 0:
            line = lineStart + '  ' + str(toCity + 1) + '   ' + str(distances[fromCity][toCity]) + '\n'
            output_file.write(line)

output_file.close()
