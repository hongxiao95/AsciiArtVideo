import cv2
import numpy as np

level = 1
[colF, ftSize, ftWidth] = [level + 2, (level + 2) * 0.15, 1 + int((level + 2) / 5)]
charSetGray =['.', ';', '-', ':', '!', '>', '7', '?', 'C', 'O', '$', 'Q', 'H', 'N', 'M', 'M']
cap = cv2.VideoCapture("SituMovie1.mp4")
sourceWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
sourceHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
sourceFrameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
sourceFPS = int(cap.get(cv2.CAP_PROP_FPS))
outWidth = 1280
outHeight = int(sourceHeight * (outWidth / sourceWidth))

print("prepare paint......")
outImg = cv2.cvtColor(np.uint8([[0 for i in range(outWidth)] for j in range(outHeight)]), cv2.COLOR_GRAY2RGB)
fcc = cv2.VideoWriter_fourcc('X','V','I','D')
writer = cv2.VideoWriter("BlackBoard.avi", fcc, sourceFPS, (outWidth, outHeight))
for i in range(sourceFrameCount):
    writer.write(outImg)
writer.release()
capOut = cv2.VideoCapture("BlackBoard.avi")
outImgs = []
for fr in range(sourceFrameCount):
    _, outImg = capOut.read()
    outImgs.append(outImg)
print("Canvas ready\n")

for fr in range(sourceFrameCount):
    _, srcImg = cap.read()
    srcArray = np.uint8(srcImg)
    for i in range(0, sourceHeight, colF):
        for j in range(0, sourceWidth, colF):
            cv2.putText(outImgs[fr], charSetGray[int((sum(srcArray[i][j]) / 3) / 17)],(j * 4, i * 4), cv2.FONT_HERSHEY_SIMPLEX, ftSize, (255,255,255), ftWidth)
    cv2.putText(outImgs[fr], "by H LaoBan", (600, 600), cv2.FONT_HERSHEY_SIMPLEX,
                3, (0, 60, 255), 3)
    print("finished: %.2f %%" % (fr/sourceFrameCount * 100)) if fr & 15 == 0 else 0

writer = cv2.VideoWriter("SituWechat1.avi", fcc, sourceFPS, (outWidth, outHeight))
for i in range(sourceFrameCount):
    writer.write(outImgs[i])
    print(i, "of", sourceFrameCount) if i & 15 == 0 else 0
writer.release()
print("All finished")