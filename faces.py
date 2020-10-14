"""import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()"""

# Python program to explain time.time_ns() method

# importing time module
import time
# Get the time in seconds
# since the epoch
# using time.time() method
time_sec = time.time()

# Get the time in nanoseconds
# since the epoch
# using time.time_ns() method
time_start = time.time_ns()

print("hello world")

time_end = time.time_ns()

print(time_end-time_start)