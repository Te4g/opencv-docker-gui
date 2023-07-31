import sys
import cv2

mouse_position = [0, 0]

def get_mouse_position(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_position[0] = x
        mouse_position[1] = y


def run(file_path: str):
    cap = cv2.VideoCapture(file_path)
    cv2.namedWindow('Video')

    if not cap.isOpened():
        print("Error opening video stream or file")
        exit(1)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.setMouseCallback('Video', get_mouse_position)

            overlay = frame.copy()
            x, y = mouse_position
            cv2.circle(overlay, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(
                overlay,
                f'({x}, {y})',
                (x - 30, y + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
                cv2.LINE_AA
            )

            alpha = 1
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        run(file_path=file_path)
    except Exception as e:
        print(f'Error: {e}')
