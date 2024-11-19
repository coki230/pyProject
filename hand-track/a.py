import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

hand_model = mp.solutions.hands.Hands()
draw_util = mp.solutions.drawing_utils

def get_distance(point1, point2):
    # return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
    return (point1.x - point2.x) * 100 ** 2 + (point1.y - point2.y) * 100 ** 2


def get_point_if_close(landmark_list):
    distance = get_distance(landmark_list[4], landmark_list[8])
    if distance < 300:
        return landmark_list[4]
    else:
        return None


while True:
    is_ok, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hand_model.process(img_rgb)
    h, w, _ = img_rgb.shape

    # if result.multi_hand_landmarks:
    #     for hand_id, landmarks in enumerate(result.multi_hand_landmarks):
    #         # draw_util.draw_landmarks(img, landmark, mp.solutions.hands.HAND_CONNECTIONS)
    #         landmark_list = landmarks.landmark
    #         distance = get_distance(landmark_list[4], landmark_list[8])
    #         print(distance)

    if result.multi_hand_landmarks and len(result.multi_hand_landmarks) > 1:
        # for hand_id, landmarks in enumerate(result.multi_hand_landmarks):
        #     # draw_util.draw_landmarks(img, landmark, mp.solutions.hands.HAND_CONNECTIONS)
        #     landmark_list = landmarks.landmark
        #     distance = get_distance(landmark_list[4], landmark_list[8])
        #     print(distance)
        #     # for id, landmark in enumerate(landmark_list):
        #     #     cv2.putText(img, str(id), (int(landmark.x * w), int(landmark.y * h)), cv2.FONT_ITALIC, 1, (255, 0, 0), 2, cv2.QT_STYLE_NORMAL)
        #     #     cv2.circle(img, (int(landmark.x * w), int(landmark.y * h)), 1, (255, 0, 0), 3, cv2.QT_STYLE_NORMAL)
        #     #     print(id, landmark)
        point1 = get_point_if_close(result.multi_hand_landmarks[0].landmark)
        point2 = get_point_if_close(result.multi_hand_landmarks[1].landmark)
        if point1 is not None and point2 is not None:
            cv2.line(img, (int(point1.x * w), int(point1.y * h)), (int(point2.x * w), int(point2.y * h)), (255, 0, 0), 2, cv2.QT_STYLE_NORMAL)


    img = cv2.flip(img, 1)
    cv2.imshow("img", img)
    cv2.waitKey(1)