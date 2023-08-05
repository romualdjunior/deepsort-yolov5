import cv2
import streamlit as st
from deep_list import *
import torch
import os
from pathlib import Path
import sys

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def main():
    st.title("Dashboard")
    st.markdown(
        "In this application we are using **YoloV5** for detecting and classifying objects and **Deepsort** for tracking their movements. Click on the Start tracking button below for the default RTSP Link to work and if you want, you can provide a video link or upload a local one. After clicking on the tracking button, wait for few seconds for the video to load..."
    )

    inference_msg = st.empty()
    st.sidebar.title("Configuration")

    input_source = st.sidebar.radio("Select input source", ("RTSP", "Local video"))

    conf_thres = st.sidebar.text_input("Class confidence threshold", "0.25")

    conf_thres_drift = st.sidebar.text_input(
        "Class confidence threshold for drift dectection", "0.75"
    )

    fps_drop_warn_thresh = st.sidebar.text_input("FPS drop warning threshold", "8")

    save_output_video = st.sidebar.radio("Save output video?", ("Yes", "No"))
    if save_output_video == "Yes":
        nosave = False
        display_labels = False
    else:
        nosave = True
        display_labels = True

    save_poor_frame = st.sidebar.radio("Save poor performing frames?", ("Yes", "No"))
    if save_poor_frame == "Yes":
        save_poor_frame__ = True
    else:
        save_poor_frame__ = False

    # ------------------------- LOCAL VIDEO ------------------------------
    if input_source == "Local video":
        video = st.sidebar.file_uploader(
            "Select input video", type=["mp4", "avi"], accept_multiple_files=False
        )

        if st.sidebar.button("Start tracking"):

            stframe = st.empty()

            st.subheader("Inference Stats")
            kpi1, kpi2, kpi3 = st.columns(3)

            st.subheader("System Stats")
            js1, js2, js3 = st.columns(3)

            # Updating Inference results

            with kpi1:
                st.markdown("**Frame Rate**")
                kpi1_text = st.markdown("0")
                fps_warn = st.empty()

            with kpi2:
                st.markdown("**Detected objects in curret Frame**")
                kpi2_text = st.markdown("0")

            with kpi3:
                st.markdown("**Total Detected objects**")
                kpi3_text = st.markdown("0")

            # Updating Jetson stats

            with js1:
                st.markdown("**Memory usage**")
                js1_text = st.markdown("0")

            with js2:
                st.markdown("**CPU Usage**")
                js2_text = st.markdown("0")

            with js3:
                st.markdown("**GPU Memory Usage**")
                js3_text = st.markdown("0")

            st.subheader("Inference Overview")
            inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

            with inf_ov_1:
                st.markdown(
                    "**Poor performing classes (Conf < {0})**".format(conf_thres_drift)
                )
                inf_ov_1_text = st.markdown("0")

            with inf_ov_2:
                st.markdown("**No. of poor peforming frames**")
                inf_ov_2_text = st.markdown("0")

            with inf_ov_3:
                st.markdown("**Minimum FPS**")
                inf_ov_3_text = st.markdown("0")

            with inf_ov_4:
                st.markdown("**Maximum FPS**")
                inf_ov_4_text = st.markdown("0")

            video_name = video.name
            video_extention = video_name.split(".")[-1]
            with open(os.path.join("upload", "input." + video_extention), "wb") as f:
                f.write(video.getbuffer())
            detect(
                weights="yolov5s_people.pt",
                source="upload/input." + video_extention,
                stframe=stframe,
                kpi1_text=kpi1_text,
                kpi2_text=kpi2_text,
                kpi3_text=kpi3_text,
                js1_text=js1_text,
                js2_text=js2_text,
                js3_text=js3_text,
                conf_thres=float(conf_thres),
                device="0",
                nosave=nosave,
                display_labels=display_labels,
                conf_thres_drift=float(conf_thres_drift),
                save_poor_frame__=save_poor_frame__,
                inf_ov_1_text=inf_ov_1_text,
                inf_ov_2_text=inf_ov_2_text,
                inf_ov_3_text=inf_ov_3_text,
                inf_ov_4_text=inf_ov_4_text,
                fps_warn=fps_warn,
                fps_drop_warn_thresh=float(fps_drop_warn_thresh),
            )
            inference_msg.success("Inference Complete!")

    # -------------------------- WEBCAM ----------------------------------
    if input_source == "Webcam":

        if st.sidebar.button("Start tracking"):

            stframe = st.empty()

            st.subheader("Inference Stats")
            kpi1, kpi2, kpi3 = st.columns(3)

            st.subheader("System Stats")
            js1, js2, js3 = st.columns(3)

            # Updating Inference results

            with kpi1:
                st.markdown("**Frame Rate**")
                kpi1_text = st.markdown("0")
                fps_warn = st.empty()

            with kpi2:
                st.markdown("**Detected objects in curret Frame**")
                kpi2_text = st.markdown("0")

            with kpi3:
                st.markdown("**Total Detected objects**")
                kpi3_text = st.markdown("0")

            # Updating Jetson stats

            with js1:
                st.markdown("**Memory usage**")
                js1_text = st.markdown("0")

            with js2:
                st.markdown("**CPU Usage**")
                js2_text = st.markdown("0")

            with js3:
                st.markdown("**GPU Memory Usage**")
                js3_text = st.markdown("0")

            st.subheader("Inference Overview")
            inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

            with inf_ov_1:
                st.markdown(
                    "**Poor performing classes (Conf < {0})**".format(conf_thres_drift)
                )
                inf_ov_1_text = st.markdown("0")

            with inf_ov_2:
                st.markdown("**No. of poor peforming frames**")
                inf_ov_2_text = st.markdown("0")

            with inf_ov_3:
                st.markdown("**Minimum FPS**")
                inf_ov_3_text = st.markdown("0")

            with inf_ov_4:
                st.markdown("**Maximum FPS**")
                inf_ov_4_text = st.markdown("0")

            detect(
                weights="yolov5s_people.pt",
                source="0",
                stframe=stframe,
                kpi1_text=kpi1_text,
                kpi2_text=kpi2_text,
                kpi3_text=kpi3_text,
                js1_text=js1_text,
                js2_text=js2_text,
                js3_text=js3_text,
                conf_thres=float(conf_thres),
                device="0",
                nosave=nosave,
                display_labels=display_labels,
                conf_thres_drift=float(conf_thres_drift),
                save_poor_frame__=save_poor_frame__,
                inf_ov_1_text=inf_ov_1_text,
                inf_ov_2_text=inf_ov_2_text,
                inf_ov_3_text=inf_ov_3_text,
                inf_ov_4_text=inf_ov_4_text,
                fps_warn=fps_warn,
                fps_drop_warn_thresh=float(fps_drop_warn_thresh),
            )

    # -------------------------- RTSP ------------------------------
    if input_source == "RTSP":

        rtsp_input = st.sidebar.text_input(
            "Video Link or Camera IP Address",
            "https://portfolio2.nyc3.digitaloceanspaces.com/cctv.mp4",
        )
        if st.sidebar.button("Start tracking"):

            stframe = st.empty()

            st.subheader("Inference Stats")
            kpi1, kpi2, kpi3 = st.columns(3)

            st.subheader("System Stats")
            js1, js2, js3 = st.columns(3)

            # Updating Inference results

            with kpi1:
                st.markdown("**Frame Rate**")
                kpi1_text = st.markdown("0")
                fps_warn = st.empty()

            with kpi2:
                st.markdown("**Detected objects in curret Frame**")
                kpi2_text = st.markdown("0")

            with kpi3:
                st.markdown("**Total Detected objects**")
                kpi3_text = st.markdown("0")

            # Updating Jetson stats

            with js1:
                st.markdown("**Memory usage**")
                js1_text = st.markdown("0")

            with js2:
                st.markdown("**CPU Usage**")
                js2_text = st.markdown("0")

            with js3:
                st.markdown("**GPU Memory Usage**")
                js3_text = st.markdown("0")

            st.subheader("Inference Overview")
            inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

            with inf_ov_1:
                st.markdown(
                    "**Poor performing classes (Conf < {0})**".format(conf_thres_drift)
                )
                inf_ov_1_text = st.markdown("0")

            with inf_ov_2:
                st.markdown("**No. of poor peforming frames**")
                inf_ov_2_text = st.markdown("0")

            with inf_ov_3:
                st.markdown("**Minimum FPS**")
                inf_ov_3_text = st.markdown("0")

            with inf_ov_4:
                st.markdown("**Maximum FPS**")
                inf_ov_4_text = st.markdown("0")

            detect(
                weights="yolov5s_people.pt",
                source=rtsp_input,
                stframe=stframe,
                kpi1_text=kpi1_text,
                kpi2_text=kpi2_text,
                kpi3_text=kpi3_text,
                js1_text=js1_text,
                js2_text=js2_text,
                js3_text=js3_text,
                conf_thres=float(conf_thres),
                device="0",
                nosave=nosave,
                display_labels=display_labels,
                conf_thres_drift=float(conf_thres_drift),
                save_poor_frame__=save_poor_frame__,
                inf_ov_1_text=inf_ov_1_text,
                inf_ov_2_text=inf_ov_2_text,
                inf_ov_3_text=inf_ov_3_text,
                inf_ov_4_text=inf_ov_4_text,
                fps_warn=fps_warn,
                fps_drop_warn_thresh=float(fps_drop_warn_thresh),
            )

    torch.cuda.empty_cache()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
