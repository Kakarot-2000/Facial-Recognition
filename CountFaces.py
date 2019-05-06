# Find the number of faces in an image
import face_recognition

# Load the image that needs to be analyzed
groupImage = face_recognition.load_image_file('./Images/group1.jpg')

# Get an array of coordinates for each face in the image
faceCoordinates = face_recognition.face_locations(groupImage)

# Print the number of faces from the array
print(f'There are {len(faceCoordinates)} people in this image')
