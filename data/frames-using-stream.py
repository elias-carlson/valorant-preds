from vidgear.gears import CamGear
import cv2
import sys
import os

link = sys.argv[1]
folder = sys.argv[2] if sys.argv[2] else "new_frames"

stream = CamGear(source=link,
                 stream_mode=True,
                 time_delay=0).start()

fps = 60
secsBetween = 5

currentFrame = 0
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}
    # if currentFrame % 30 == 0:
    if not os.path.exists(folder):
        os.mkdir(folder)
        
    fileName = f"{folder}/frame{currentFrame}.jpg"
    if currentFrame % (secsBetween * fps) == 0:
        print(f"Writing frame {currentFrame} to {fileName}!")
        if not cv2.imwrite(fileName, frame):
            print(f"Failed to write frame {currentFrame}")
            break
            # print(f"Wrote frame {currentFrame}!")
        

    currentFrame += 1

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()