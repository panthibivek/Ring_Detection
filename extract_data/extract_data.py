
import cv2
import os

fps = 3

class ExtractTrainingData:
    def __init__(self, input_video_path : str):
        self.input_video_path = input_video_path
        current_file_path = os.path.dirname(os.path.abspath("__file__"))
        only_dir = sorted([f for f in os.listdir(current_file_path) if os.path.isdir(os.path.join(current_file_path, f))])
        last_dir = ""
        for dir_name in only_dir:
            if "run" in dir_name:
                last_dir = dir_name
        if len(only_dir) == 0 or last_dir == "":
            last_seq_number = 0
        else:
            last_seq_number =  int(only_dir[-1][-1])
        self.current_output_dir = current_file_path + "/run" + str(last_seq_number+1)
        os.mkdir(self.current_output_dir)
        self.file_count = 1
        self.run_through_each_file()

    def run_through_each_file(self):
        only_dir = sorted([f for f in os.listdir(self.input_video_path) if os.path.isfile(os.path.join(self.input_video_path, f))])
        for each_file in only_dir:
            self.get_photoes(self.input_video_path + "/" + each_file)

    def get_photoes(self, video_file : str):
        video_cap_obj = cv2.VideoCapture(video_file)
        total_frames = int(video_cap_obj.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = int(video_cap_obj.get(cv2.CAP_PROP_FPS) / fps)
        current_frame = 0
        while current_frame < total_frames:
            ret, frame = video_cap_obj.read()
            if ret:
                if current_frame % frame_interval == 0:
                    cv2.imwrite(self.current_output_dir + "/image" + str(self.file_count) + ".jpg", frame)
                    self.file_count += 1
                current_frame += 1
            else:
                break
        video_cap_obj.release()

data_obj = ExtractTrainingData(os.path.dirname(os.path.abspath("__file__")) + "/new_training_video")

