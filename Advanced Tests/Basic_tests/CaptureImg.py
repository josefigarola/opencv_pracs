#------------------------------------------------------------------------------------------------------------------
#   Image capture program
#------------------------------------------------------------------------------------------------------------------
import cv2
import pickle
from datetime import datetime

# Initialize camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# Read images
n_images = 50
images = []
for i in range(n_images):
    
    print("Image #", i+1)
    input("Press enter to take picture...")    
    result, image = cam.read()
  
    # Show result
    if result:  
        images.append(image)
        cv2.imshow("Image #" + str(i+1), image)         
        cv2.waitKey(0)
        cv2.destroyWindow("Image #" + str(i+1)) 
    
    else:
        print("No image detected")

# Save data
now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
outputFile = open(now + '.obj', 'wb')
pickle.dump(images, outputFile)
outputFile.close()


#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------















