# Extract, display, and save all faces in a given image
import face_recognition
from PIL import Image

# Group image
groupImage = face_recognition.load_image_file('./Images/group1.jpg')
faceCoordinates = face_recognition.face_locations(groupImage)

# Loop through the different faces found
for faceCoordinate in faceCoordinates:
    top, right, bottom, left = faceCoordinate

    faceImageArray = image[top:bottom, left:right] # Gives the face image in the form of an array
    faceImage = Image.fromarray(imageArray) # Use PIL library to get the image from an array
    
    faceImage.show() # Show each face found
    
    # Save the faces in their own files (according to their top coordinate)
    faceImage.save(f'{top}.jpg') 
