import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from PIL import Image, ImageTk
import json
from utils.vision import predict_constellation
from collections import deque, Counter

prediction_queue = deque(maxlen=10)

cap = None
running = False

def start_camera():
    global cap, running
    cap = cv2.VideoCapture(0)
    running = True
    update_frame()

def stop_camera():
    global cap, running
    running = False
    if cap:
        cap.release()
        cam_label.config(image='')

def update_frame():
    global cap, running, prediction_queue
    if cap and running:
        ret, frame = cap.read()
        if ret:
            # Predict and add to queue
            label = predict_constellation(frame)
            prediction_queue.append(label)

            # Use the most frequent prediction in the queue
            most_common = Counter(prediction_queue).most_common(1)[0][0]

            # Draw prediction
            cv2.putText(frame, f"Prediction: {most_common}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            cam_label.imgtk = imgtk
            cam_label.configure(image=imgtk)

        cam_label.after(10, update_frame)


def show_quiz():
    with open("quizzes/questions.json") as f:
        data = json.load(f)["questions"]

    score = 0
    for q in data:
        answer = tk.simpledialog.askstring("Quiz", f"{q['question']}\nOptions: {', '.join(q['options'])}")
        if answer and answer.strip().lower() == q["answer"].lower():
            score += 1

    messagebox.showinfo("Quiz Result", f"You scored {score} out of {len(data)}")

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error", "Failed to load image.")
        return

    label = predict_constellation(image)
    image = cv2.resize(image, (640, 480))
    cv2.putText(image, f"Prediction: {label}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    cam_label.imgtk = imgtk
    cam_label.configure(image=imgtk)

    messagebox.showinfo("Prediction", f"This image is predicted as: {label}")

root = tk.Tk()
root.title("AstroVision")
root.geometry("900x700")
root.configure(bg="black")

cam_label = tk.Label(root, bg="black")
cam_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

tk.Button(btn_frame, text="Start Camera", command=start_camera, bg="green", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Stop Camera", command=stop_camera, bg="red", fg="white", width=15).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Take Quiz", command=show_quiz, bg="blue", fg="white", width=15).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="Upload Image", command=upload_image, bg="orange", fg="white", width=15).grid(row=0, column=3, padx=10)

root.mainloop()
