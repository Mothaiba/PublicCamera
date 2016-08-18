import Constants
import requests
# class Node:
#     def __init__(self, id, timeList, crowdIndexList, imageURL):
#         self.id = id
#         self.timeList = timeList
#         self.crowdIndexList = crowdIndexList
#         self.imageURL = imageURL

class Project:
    def __init__(self, id):
        self.id = id

class Floor:
    def __init__(self, id, crowdIndex):
        self.id = id
        self.crowdIndex = crowdIndex

class Node:
    def __init__(self, id, label, fileUrl):
        self.id = id
        self.label = label
        self.fileUrl = fileUrl
        self.localImagePath = None
        self.data = None
        self.datetime = None

        if self.fileUrl != '':
            image_url = 'http://img.v3.news.zdn.vn/w660/Uploaded/Yfrur/2016_05_12/avay.JPG'
            img_data = requests.get(image_url).content
            self.localImagePath = Constants.LOCAL_IMAGE_FOLDER + str(self.id) + '.jpg'
            with open(self.localImagePath, 'wb') as handler:
                handler.write(img_data)

    def setData(self, data, time):
        self.data = data
        self.datetime = time