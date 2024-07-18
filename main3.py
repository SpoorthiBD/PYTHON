import cv2

def main():
    try:
        # Attempt to open the video device (default camera)
        cap = cv2.VideoCapture(0)  # Use 0 for default camera

        if not cap.isOpened():
            raise IOError("Error: Could not open video device")

        # Process the video feed
        while True:
            ret, frame = cap.read()
            if not ret:
                raise IOError("Error: Failed to read frame from video device")

            # Display the frame
            cv2.imshow('Frame', frame)

            # Exit loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture object and close any OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
