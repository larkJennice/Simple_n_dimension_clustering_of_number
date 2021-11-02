# Simple_n_dimension_coordinates_clustering

* This is a project for clustering points in different dimensions. (For instance, 3-dimensions means that the data that have 3 coordinates x, y, z)
# Training
* It computes the centroid of each class
* It constucts a discriminant function between each pari of classes.
* In general, it s a "basic linear classifier".

# Testing
* For testing, this clustering project utilizes the discriminant function to decide the categories.
* For instance, it first deciedes "X or Y" and then decide "X or Z" or "Y or Z" by giving priority to class X, then Y, then Z.

# Extra Funcitonality
* It keeps tract of true positives (TP), true negatives (TN), false positives (FP), false negatives (FN).
