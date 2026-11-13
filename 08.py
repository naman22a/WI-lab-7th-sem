def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)

    union = set1.union(set2)

    if len(union) == 0:
        return 1.0

    similarity = len(intersection) / len(union)

    return similarity


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

similarity = jaccard_similarity(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", set1.intersection(set2))
print("Union:", set1.union(set2))
print("Jaccard Similarity:", similarity)
print("Jaccard Distance:", 1 - similarity)
