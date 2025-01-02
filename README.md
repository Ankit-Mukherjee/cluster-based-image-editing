# Image Compression and Recoloring using K-Means and kNN

This project demonstrates the application of **k-means clustering** for image compression and **k-nearest neighbors (kNN)** for recoloring a second image based on the compressed palette of the first image. By grouping similar colors, this approach reduces the size of images while maintaining their visual quality.

## Features
1. Compress an image by grouping its colors into a limited number of clusters using **k-means clustering**.
2. Apply the compressed color palette of the first image to recolor a second image using **kNN**.
3. Visualize the **Elbow Method** for determining the optimal number of clusters (`k`) for k-means.

---

## Installation

To run this project, ensure you have Python installed along with the following libraries:
- `Pillow`
- `NumPy`
- `Scikit-learn`
- `Matplotlib`

Install the dependencies using pip:
```bash
pip install Pillow numpy scikit-learn matplotlib
```
## Usage
1. Clone the repository
2. Place the images you want to process (image1.png and image2.png) in the project folder.
3. Run the Code
```bash
python image_edit.py
```
The following outputs will be generated:
	-	image1_done.png: Compressed version of image1.png.
	-	image2_done.png: Recolored version of image2.png using the color palette from image1.png.

 
## Implementation Details
### Key Steps
	1.	Optimal k Selection:
	-	The Elbow Method is used to determine the optimal number of clusters.
	-	A graph of within-cluster sum of squares (WCSS) vs. the number of clusters is plotted to identify the “elbow point.”
	2.	Image Compression:
	-	k-means is applied to image1 to cluster colors.
	-	Each pixel’s color is replaced with the centroid of its cluster, resulting in a compressed image.
	3.	Image Recoloring:
	-	The centroids obtained from image1 are used to recolor image2.
	-	kNN maps the colors of image2 to the closest centroids from image1.
