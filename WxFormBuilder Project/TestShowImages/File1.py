# import modules
import wx
import cv2
import gui as gui
import os
from os import listdir
from os.path import isfile, join
import File2

# define global variables

class ShowFullImageFrame(gui.FullImageDialog):
    def __init__(self):
        gui.FullImageDialog.__init__(self, None)
        self.frame = wx.Frame(None, title = 'Zoom')

    def ShowImage(self, _imageURL):
        image = wx.Image(_imageURL, wx.BITMAP_TYPE_ANY)
        self.image_full.SetBitmap(wx.BitmapFromImage(image))

def getFrame(BaseFrame):
    class ShowCamerasFrame(BaseFrame):

        PHOTO_MAX_WIDTH = 500
        IMAGE_CONTAINERS = {}
        _images = []

        # constructor
        def __init__(self):
            # initialize parent class
            BaseFrame.__init__(self, None)
            self.frame = wx.Frame(None, title = 'All Cameras')

        def loadImages(self, path):
            self.panel = wx.Panel(self.frame)

            self._images = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

            for i in range (0, len(self._images)):
                _imgContainer = "image_" +  str(i + 1)
                image = wx.Image(self._images[i], wx.BITMAP_TYPE_ANY)
                image = self.toResizeImage(image)
                self.__getattribute__(_imgContainer).SetBitmap(wx.BitmapFromImage(image))

                self.IMAGE_CONTAINERS[self.__getattribute__(_imgContainer).GetId()] = i


        def toResizeImage(self, image):
            w = image.GetWidth()
            h = image.GetHeight()

            if w > self.PHOTO_MAX_WIDTH:
                newW = self.PHOTO_MAX_WIDTH
                newH = h * self.PHOTO_MAX_WIDTH / w
                image = image.Scale(newW, newH)

            return image

        def leftDClickFunc(self, event):
            _id = event.GetId()
            imageId = self.IMAGE_CONTAINERS[_id]
            imageURL = self._images[imageId]

            imageDialog = ShowFullImageFrame()
            imageDialog.ShowImage(imageURL)
            imageDialog.Show(True)

    return ShowCamerasFrame

def toBlurImages(inPath, outPath):

    makeEmpty(outPath)

    _images = [f for f in listdir(inPath) if isfile(join(inPath, f))]

    for _image in _images:
        image  = cv2.imread(join(inPath, _image))
        result_image = image.copy()

        # Specify the trained cascade classifier
        face_cascade_name = './haarcascade/haarcascade_frontalface_alt.xml'

        # Create a cascade classifier
        face_cascade = cv2.CascadeClassifier()

        # Load the specified classifier
        face_cascade.load(face_cascade_name)

        # Preprocess the image
        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayimg = cv2.equalizeHist(grayimg)

        # Run the classifiers
        faces = face_cascade.detectMultiScale(grayimg, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, (30, 30))

        # print "Faces detected"

        if len(faces) != 0:  # If there are faces in the images
            for f in faces:  # For each face in the image

                # Get the origin co-ordinates and the length and width till where the face extends
                x, y, w, h = [v for v in f]

                # get the rectangle img around all the faces
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 5)
                sub_face = image[y:y + h, x:x + w]
                # apply a gaussian blur on this new recangle image
                sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
                # merge this blurry rectangle to our final image
                result_image[y:y + sub_face.shape[0], x:x + sub_face.shape[1]] = sub_face
                # face_file_name = "./face_" + str(y) + ".jpg"
                # cv2.imwrite(face_file_name, sub_face)

        # cv2.imshow("Detected face", result_image)
        # print join(outPath, _image)
        cv2.imwrite(join(outPath, _image), result_image)

def makeEmpty(path):
    _files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    for _file in _files:
        os.remove(_file)

def processCamera():
    # Obligatory
    app = wx.App(False)

    # '/var/www/html/publiccamera/upload/files/'
    inPath = 'C:\Users\Champ\Documents\WxFormBuilder Project\TestShowImages\images'
    outPath = r'C:\Users\Champ\Documents\WxFormBuilder Project\TestShowImages\blurred_images'



    toBlurImages(inPath, outPath)
    _images = [join(outPath, f) for f in listdir(outPath) if isfile(join(outPath, f))]

    if len(_images) == 4:
        Frame = getFrame(gui.MainFrame4)
    elif len(_images) == 5:
        Frame = getFrame(gui.MainFrame5)

    # create an object of CalcFrame
    frame = Frame()

    frame.loadImages(outPath)

    # show the frame
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':

    # processCamera()
    File2.drawChart()
