# Compare two images and see if it's the same person
import face_recognition

# First image
firstImage = face_recognition.load_image_file('./Images/Known/steph-curry.jpg')
firstImageEncoding = face_recognition.face_encodings(firstImage)[0]

# Second image
secondImage = face_recognition.load_image_file('./Images/Unknown/lebron-james.jpg') # Alternate image: './Images/Unknown/steph-curry-2.jpg' (for successful match)
secondImageEncoding = face_recognition.face_encodings(secondImage)[0]

# Compare the two image encodings (returns true for a match and false for no match)
isSamePerson = face_recognition.compare_faces([firstImageEncoding], secondImageEncoding)[0]

if isSamePerson:
    print('Both images are of the same person.')
else:
    print('Both images are not of the same person.')
