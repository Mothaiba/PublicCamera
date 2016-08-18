import Requests as R
import Classes
import Constants
import matplotlib.pyplot as plt
import requests

def getTime(dates):
    times = []
    for date in dates:
        time = date[(len(date) - 8) : ]
        times.append(time)
    return times

def getProjects():
    API_URL = Constants.API_HOST + Constants.PROJECTS
    r = requests.get(API_URL);

    if(r.status_code != 200):
        return None

    projectDict = {}
    items = r.json().get('items')

    for item in items:
        id = item.get('id')
        project = Classes.Project(id)
        projectDict[id] = project

    return projectDict

def get_FloorDict_from_SearchByProject(projectId):
    API_URL = Constants.API_HOST + Constants.SEARCH_BY_PROJECT + '?' + 'projectId=' + str(projectId)
    r = requests.get(API_URL)

    if r.status_code != 200:
        return None

    floorDict = {}
    items = r.json().get('items')

    for item in items:
        id = item.get('id')
        crowdObject = item.get('latestCrowdIndex')
        if crowdObject != None:
            crowdIndex =  crowdObject.get('value')
        else:
            crowdIndex = -1
        floor = Classes.Floor(id, crowdIndex)
        floorDict[id] = floor

    return floorDict

def get_NodeDict_from_searchByFloor(floorId):
    API_URL = Constants.API_HOST + Constants.SEARCH_BY_FLOOR + '?' + 'floorId=' + str(floorId)
    r = requests.get(API_URL)

    if r.status_code != 200:
        return None

    nodeDict = {}
    items = r.json().get('items')

    for item in items:
        id = item.get('id')
        label = item.get('label')
        lastestNodeFile = item.get('latestNodeFile')
        if lastestNodeFile != None:
            fileUrl = lastestNodeFile.get('fileUrl')
        else:
            fileUrl = None
        node = Classes.Node(id, label, fileUrl)

        nodeDict[id] = node

    return nodeDict

def testGetNodes():
    pjs = getProjects()

    for pId in pjs.keys():
        fls = get_FloorDict_from_SearchByProject(pId)
        if fls == None:
            continue
        for fId in fls.keys():
            nds = get_NodeDict_from_searchByFloor(fId)
            if nds == None:
                continue
            for nd in nds.keys():
                print nds[nd].id
                print nds[nd].fileUrl
                print nds[nd].label

    fls = get_FloorDict_from_SearchByProject(pjs[1].id)
    print fls

    nds = get_NodeDict_from_searchByFloor(fls[2].id)
    print nds

    return nds

def appendHistoricalData(nodeDicts):

    r = R.requests.get("http://128.199.77.122/publiccamera/api/index.php/v1/node-datas")
    if(r.status_code != 200):
        print "Status code != 200"
        exit(0)

    nodeData = {}
    datetime = {}

    items = r.json().get('items')
    for item in items:
        nodeId = item.get('nodeId')
        if nodeData.has_key(nodeId) == False:
            nodeData[nodeId] = []
            datetime[nodeId] = []

        nodeData[nodeId].append(item.get('value'))
        datetime[nodeId].append(item.get('remark'))

    for nodeId in nodeData.keys():
        if nodeDicts.has_key(nodeId):
            nodeDicts[nodeId].setData(nodeData[nodeId], datetime[nodeId])

    return nodeDicts

if __name__ == '__main__':


    

    # for node in nodes.keys():
    #     x = getTime(datetime[node])
    #     y = nodes[node]
    #
    #     fig = plt.figure()
    #     ax = fig.add_subplot(1, 1, 1)
    #
    #     ax.plot(range(len(x)), y)
    #     plt.xticks(range(len(x)), x)
    #
    # plt.show()