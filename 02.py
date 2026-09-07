import numpy as np

# Define two data points
point1 = np.array([2, 3])
point2 = np.array([5, 7])

# Calculate Euclidean distance
distance = np.sqrt(np.sum((point1 - point2) ** 2))

# Calculate Euclidean similarity
similarity = 1 / (1 + distance)

print("EUCLIDEAN SIMILARITY RESULT")
print("---------------------------")

print("Data Point 1:", point1)
print("Data Point 2:", point2)
print("Euclidean Distance:", round(distance, 4))
print("Euclidean Similarity:", round(similarity, 4))
