# Week 4

This Week's README help us to prepare the environment in order to be able to code correctly for each fourth delivery. We explain the use of each python file and its respective function.

## Description by Tasks

### Task 1
We have created the python file `BlockMatchingOF()` in order to estimate the Optical Flow. We have compared the results of both sequences of Kitti with other two methods which are Lucas-Kanade and Farneback. 


### Task 2

To stabilize the sequence of frames of Traffic dataset, we have created the function `CompensateImage()`.We have implemented Morphological Transformations. We have imported some functions from OpenCV, `cv2.erode()`, `cv2.dilate()` and `cv2.morphologyEx()`.

## Execution usage
### Optical Flow (Task 1)
Execute the `task1.py` to execute the Optical Flow with our Block Matching method.
```sh
$ python task1.py
```

### Video Stabilization (Task 2)
Execute the `task2.py` to stabilize the video.
```sh
$ python task2.py
```

For Task 2.3, the scripts `task2_3_ownmethod.py` and `task2_3_LK_stabilization.py` should be run to obtain the stabilization of our own video with our method and an other implementation from the optimize Jaime’s implementation in the StackOverflow (view this [link](https://stackoverflow.com/questions/14321092/lucas-kanade-python-numpy-implementation-uses-enormous-amount-of-memory))
