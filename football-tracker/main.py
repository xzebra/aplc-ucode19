import boto3
import base64
import cv2
import csv

client = boto3.client('rekognition')
REDUCTION = 0

ball_movement = []

def save_ball_data():
    with open('lame_bolas.csv', mode='w') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(['X', 'Y', 'Height', 'Width'])
        for movement in ball_movement:
            writer.writerow([str(movement[i]) for i in range(4)])

def face_recon(jpg_bytes, frame):
    height, width, layers = frame.shape
    faces = client.detect_faces(Image={'Bytes':jpg_bytes}, Attributes=['ALL'])

    # Draw rectangle around faces
    for face in faces['FaceDetails']:    
        cv2.rectangle(frame,
                      (int(face['BoundingBox']['Left']*width),
                       int(face['BoundingBox']['Top']*height)),
                      (int((face['BoundingBox']['Left']+face['BoundingBox']['Width'])*width),
                       int((face['BoundingBox']['Top']+face['BoundingBox']['Height'])*height)),
                       (0,0,255), 2)

def track_ball(jpg_bytes, frame):
    response = client.detect_labels(
        Image={
            'Bytes': jpg_bytes,
        },
        MaxLabels=123,
        MinConfidence=50,
    )
    #print([r['Name'] for r in response['Labels']])
    height, width, layers = frame.shape
    # Soccer Ball detected
    for r in response['Labels']:
        if r['Name'] == 'Soccer Ball':
            for i in r['Instances']:
                x = i['BoundingBox']['Left']*width
                x_width = i['BoundingBox']['Width']*width
                y = i['BoundingBox']['Top']*height
                y_height = i['BoundingBox']['Height']*height
                pos = [int(x + x_width/2), int(y + y_height/2)]
                ball_movement.append([pos[0], pos[1], x_width, y_height])
                cv2.circle(frame, (pos[0],pos[1]), 10, (0,0,255), -1)

def labelFrame(jpg, frame, video):
    jpg_bytes = jpg.tobytes()

    track_ball(jpg_bytes, frame)
    #face_recon(jpg_bytes, frame)

    # Display the resulting frame
    video.write(frame)

def labelVideo(video_name):
    cap = cv2.VideoCapture(video_name)
    success, frame = cap.read()

    height, width, layers = frame.shape
    video = cv2.VideoWriter('video2.mp4', cv2.VideoWriter_fourcc(*'avc1'), 20.0, (width, height))


    while success: 
        success, buf = cv2.imencode('.jpg', frame)
        labelFrame(buf, frame, video)
        success, frame = cap.read()
    cap.release()
    video.release()
    cv2.destroyAllWindows()

    save_ball_data()


#labelFrame(open('data/example.jpg', 'rb').read())
labelVideo('data/Hd3.mp4')