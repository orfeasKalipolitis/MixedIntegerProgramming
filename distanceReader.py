
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
