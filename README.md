# number-plate-detection
# Automatic-Number-plate-detection-for-vehicles


## Automatic number plate recognition (ANPR):
Number Plate recognition, also called License Plate realization or recognition using image processing methods is a potential research area in smart cities and the Internet of Things. An exponential increase in the number of vehicles necessitates the use of automated systems to maintain vehicle information for various purposes.


![ANPR](https://github.com/Ajay-mandadi/number-plate-/assets/166850848/87030859-d40a-47e7-a568-2c4e412d4dfe)

## Implementation: 
In the proposed algorithm an efficient method for recognition of Indian vehicle number plates has been devised. We are able to deal with noisy, low illuminated, cross angled, non-standard font number plates. This work employs several image processing techniques such as, morphological transformation, Gaussian smoothing, Gaussian thresholding and Sobel edge detection method in the pre-processing stage, afterwhich number plate segmentation, contours are applied by border following and contours are filtered based on character dimensions and spatial localization. Finally we apply Optical Character Recognition (OCR) to recognize the extracted characters. The detected texts are stored in the database, further which they are sorted and made available for searching. 

This project will work efficiently in recognizing owner's vehicle in small Institutions/Housing societies/Apartments. We can further modify the code to use it in other areas where ANPR is necessary. 

![anpt1](https://github.com/Ajay-mandadi/number-plate-/assets/166850848/3fc55834-63c4-4ec2-8771-2f6e816fe895)

## PROCEDURE
Import Required Libraries: Import the necessary libraries, including OpenCV for image processing.

Upload Image: Use the files.upload() method from Google Colab to upload an image containing a vehicle with a visible number plate.

Load and Preprocess Image: Load the uploaded image using OpenCV and convert it to grayscale.

License Plate Detection: Use the CascadeClassifier from OpenCV to detect license plates in the image. You can use a pre-trained Haar cascade classifier for this purpose.

Mark License Plates: For each detected license plate, draw a rectangle around it and mark it with a green color.

Display the Image: Display the processed image with the marked license plates using the cv2_imshow method from Google Colab.



Give the path of folders "Dataset" and "Search_image" while executing [Program.py](Program.py)
## References:
* M M Shidore, and S P Narote. (2011) “Number Plate Recognition for Indian Vehicles” International Journal of Computer Science and  Network Security 11 (2): 143-146 
* Sang Kyoon Kim, D. W. Kim and Hang Joon Kim. (1996) “A recognition of vehicle license plate using a genetic algorithm based segmentation,” Proceedings of 3rd IEEE International Conference on Image Processing, Lausanne. 
* https://docs.opencv.org/master/
* https://github.com/anuj-badhwar/Indian-Number-Plate-Recognition-System
