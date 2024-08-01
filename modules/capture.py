import cv2
import time, datetime



class Capture:
    def __init__(self,camera=0):
        self.camera = camera
        self.cap = cv2.VideoCapture(camera)

    def getFileName(self):
        today = datetime.datetime.today().date()
        crntTime = str(datetime.datetime.today().time()).split('.')[0].replace(':', '')
        fileName = f"capture-{str(today)}@{crntTime}.jpg"

        return fileName

    def image(self,
              saveImage = False, filePath = ""):
        
        success , img = self.cap.read()

        if not success:
            raise RuntimeError("Camera not Found")

        if saveImage:
            fileName = filePath+ "/" + self.getFileName() if filePath else self.getFileName()
            cv2.imwrite(fileName, img)
            
        return img
    
    def displayImage(self, image, frameText = "Image Frame"):
        cv2.imshow(frameText, image)
        cv2.waitKey(1)
        return
    
    def clear(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return
    