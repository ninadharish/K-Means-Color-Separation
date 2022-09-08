# K-Means Color Separation

## Description

Given an image of a traffic signal, this project attempts to separate the image based on its color into 4 different classes using the K-Means algorithm.


## Data

* Input image of Traffic Signal

![alt text](/data/traffic_img.png)


## Approach

* Select four random RGB values

* For each pixel, find euclidean distance of RGB values from all means get the minimum

* Calculate the new means of all the classes

* Repeat the process 40 times

* Fill the class mean values to all the pixels inside the class to get the separated image


## Output

* Separated Output Image

![alt text](/output/output.png)


## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://avatars.githubusercontent.com/u/5009934?v=4&s=400" alt="opencv" width="40" height="40"/>&ensp; </a>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [OpenCV](https://opencv.org/)


### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/K-Means-Image-Color-Separation.git
```

* Open the repository and navigate to the `src` folder.
```
cd K-Means-Image-Color-Separation/src
```

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)
