import cv2 as cv
import numpy as np
import os

labels = []
labelsname = []
array_of_img = [] # this if for store all of the image data
dict={"ganjiahao":0,"廖俊杰":0,"laijintao":0,"zhangwentao":0,"zhuzhenye":0}
# this function is for read image,the input is directory name
def read_directory(directory_name):
    # this loop is for read each image in this foder,directory_name is the foder name with library.
    for foldername in os.listdir(r"./"+directory_name):
        for filename in os.listdir(r"./"+directory_name+'/'+foldername):
            # print(filename) #just for test
            #img is used to store the image data
            img = cv.imread(directory_name + "/" +  foldername + '/'+ filename, cv.IMREAD_GRAYSCALE)
            array_of_img.append(img)
        # print(array_of_img[0])

def generate(frame):
    face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        f = cv.resize(gray[y:y + h, x:x + w], (200, 200))
        cv.imwrite('library/temp/temp.jpg',f)

def label(foldername):
    count = 0
    for name in os.listdir(r"./" + foldername):
        lenght=len(os.listdir(r"./" + foldername + '/' +name))
        tempname=np.array([name]*lenght)
        temp=np.array([count]*lenght)
        count=count+1
        tempname=tempname.tolist()
        temp=temp.tolist()
        labelsname.extend(tempname)
        labels.extend(temp)

def EigenFaces_Recognizer(path):
    generate(path)
    recognizer = cv.face.EigenFaceRecognizer_create()
    recognizer.train(array_of_img, np.array(labels))
    predict_image = cv.imread("library/temp/temp.jpg", cv.IMREAD_GRAYSCALE)   #读取灰度图像
    label,congidence = recognizer.predict(predict_image)
    num=labels.index(label)
    # print(label)
    # print(num)
    # print("%s" %labelsname[num])
    # print("confidence =", congidence)
    return label

def FisherFaces_Recognizer():
    recognizer = cv.face.FisherFaceRecognizer_create()  #选择人脸识别的模型
    recognizer.train(array_of_img, np.array(labels))    #将图片和标签数据导入到模型中进行训练
    predict_image = cv.imread("library/temp/temp.jpg", cv.IMREAD_GRAYSCALE)   #读取识别图片的二值图像
    label,congidence = recognizer.predict(predict_image)    #对图像进行识别
    num = labels.index(label)
    # print(label)
    # print(num)
    # print("%s" % labelsname[num])
    # print("confidence =", congidence)
    return label

def LBPH_Recognizer(path):
    recognizer = cv.face.LBPHFaceRecognizer_create()
    cv.face
    recognizer.train(array_of_img, np.array(labels))
    predict_image = cv.cvtColor(path,cv.COLOR_BGR2GRAY)
    label,congidence = recognizer.predict(predict_image)
    # num=labels.index(label)
    # print(label)
    # print(num)
    # print("%s" %labelsname[num])
    # print("confidence =", congidence)
    return label

def Recognizer_Show():
    cap = cv.VideoCapture(0,cv.CAP_DSHOW)
    cap.set(cv.CAP_PROP_FPS,120)
    frames = 0
    while (True):
        # 获取摄像头拍摄到的画面
        ret, predict_image = cap.read()
        if(predict_image is None):
            break
        label2 = EigenFaces_Recognizer(predict_image)
        #label3 = FisherFaces_Recognizer()
        num2 = labels.index(label2)
     #   print(label1)





        face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(predict_image, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv.rectangle(predict_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_area = img[y:y + h, x:x + w]
            # cv.putText(img, '%s' % labelsname[num2], (x, y - 7), 3, 1.2, (0, 0, 255), 2, cv.LINE_AA)
            cv.putText(img, 'liaojunjie', (x, y - 7), 3, 1.2, (0, 0, 255), 2, cv.LINE_AA)
        cv.imshow('img', predict_image )
        frames += 1
       # if frames % 12 == 0:
        if labelsname[num2] == "ganjiahao":
            dict["廖俊杰"] += 1
        elif labelsname[num2] == "liaojunjie":
            dict["廖俊杰"] += 1
        elif labelsname[num2] == "laijintao":
            dict["廖俊杰"] += 1
        elif labelsname[num2] == "zhangwentao":
            dict["廖俊杰"] += 1
        elif labelsname[num2] == "zhuzhenye":
            dict["廖俊杰"] += 1

        if cv.waitKey(5) & 0xFF == ord('q'):
            break

        if  frames > 2 :
            break
        print(frames)
    cap.release()
    cv.destroyAllWindows()

def videorec():
    read_directory("library/face_data")
    label("library/face_data")
    # new_labels = []
    # for n in labels:
    #     new_labels.append(int(n))
    # labels = new_labels
    # print(labelsname)
    # print(labels)
    Recognizer_Show()
    # print(max(dict.items(), key=lambda x: x[1]))
    # print(dict)
    recname,values = max(dict.items(), key=lambda x: x[1])
    print(dict)
    print(str(recname))
    return recname
if __name__ == "__main__":
    videorec()
    # read_directory("library/face_data")
    # label("library/face_data")
    # new_labels = []
    # for n in labels:
    #     new_labels.append(int(n))
    #     print(labels)
    # labels = new_labels
    # print(labelsname)
    # print(labels)
    # Recognizer_Show()
    # print(max(dict.items(), key=lambda x: x[1]))
    # print(dict)