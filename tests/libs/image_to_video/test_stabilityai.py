import os
import time
import cv2
import pytest
import requests
from dotenv import load_dotenv
from PIL import Image
from src.libs.image_to_video.stabilityai import VideoManager

# Setting
load_dotenv()
focus_point_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
test_img_folder_path = os.path.abspath(os.path.join(focus_point_path, "test_img"))
NO_TOKEN_ID_KEY = os.environ.get("STABILITY_AI_NO_TOKEN_KEY", 'utf-8')
TOKEN_KEY = os.environ.get("STABILITY_AI_NO_TOKEN_KEY", 'utf-8')

# Mockup
IMG_PATH = os.path.abspath(os.path.join(test_img_folder_path, "origin_img.jpg"))
SEED = 0
CFG_SCALE = 2.5
MOTION_BUCKET_ID=40
GENERATED_ID="bb8216b8ac65f2d91ed5ceedb496d24b63e2be55f389582080619b22d7694b8d"
GENERATE_ORIGIN_VIDEO_PATH = os.path.abspath(os.path.join(test_img_folder_path, "origin_video.mp4"))
REVERSED_VIDEO_PATH = os.path.abspath(os.path.join(test_img_folder_path, "reversed_video.mp4"))
SLOW_VIDEO_PATH = os.path.abspath(os.path.join(test_img_folder_path, "slow_video.mp4"))


# @pytest.mark.order(1)
# @pytest.mark.asyncio
# async def test_can_resize_image():
#     # given : 유효한 이미지
#     # when : 이미지 사이즈 변경 요청
#     resize_image_path = VideoManager(test_img_folder_path).resize_image("origin_img.jpg")

#     # then : 이미지 저장 파일 확인
#     assert os.path.exists(resize_image_path)


# @pytest.mark.order(2)
# @pytest.mark.asyncio
# async def test_can_request_generate_video():
#     # given : 유효한 토큰 + 이미지
#     # RESIZED_IMAGE_PATH = os.path.abspath(os.path.join(test_img_folder_path, "resized_img.jpg"))
#     # when : 비디오 생성 요청
#     response = VideoManager(test_img_folder_path).post_generated_video("resized_img.jpg")
#     print(response.json())
#     assert response.status_code == 200
#     assert len(response.json()["id"]) > 0


# def test_cannot_request_generate_video_with_non_token():
#     # given : 토큰 부족 + 이미지
#     IMG_PATH = os.path.abspath(os.path.join(test_img_path, "test.png"))

#     # when : 비디오 생성 요청
#     response = requests.post(
#         "https://api.stability.ai/v2alpha/generation/image-to-video",
#         headers={
#             "authorization": "Bearer "+ NO_TOKEN_ID_KEY,
#         },
#         data={
#             "seed": SEED,
#             "cfg_scale": CFG_SCALE,
#             "motion_bucket_id": MOTION_BUCKET_ID
#         },
#         files={
#             "image": ("file", open(IMG_PATH, "rb"), "image/png")
#         },
#     )

#     # then : 토큰 부족 메시지
#     print(response.json())
#     assert response.status_code == 404


# def test_cannnot_request_generate_video_with_non_image():
#     # given : 유효한 토큰 + 이미지 없음
#     no_image_path = os.path.abspath(os.path.join(test_img_path, "no_image.jpg"))

#     # when : 비디오 생성 요청
#     # then : 이미지 없음 메시지
#     with pytest.raises(FileNotFoundError):
#         response = requests.post(
#             "https://api.stability.ai/v2alpha/generation/image-to-video",
#             headers={
#                 "authorization": "Bearer " + TOKEN_KEY,
#             },
#             data={
#                 "seed": SEED,
#                 "cfg_scale": CFG_SCALE,
#                 "motion_bucket_id": MOTION_BUCKET_ID
#             },
#             files={
#                 "image": ("file", open(no_image_path, "rb"), "image/png")
#             },
#         )
#         assert response.status_code == 200


# @pytest.mark.order(3)
# def test_can_get_generated_video():
#     # given : 생성된 비디오 요청 id
#     # when : 비디오 전달 요청
#     generated_origin_path = VideoManager(
#         test_img_folder_path).get_generated_video(GENERATED_ID, "origin_video.mp4")

#     # then : 비디오 전달 확인
#     assert os.path.exists(generated_origin_path)

# def reverse_generated_video(output_video: cv2.VideoWriter, reverse: bool = False):
#     # 비디오 캡쳐 객체 생성
#     cap = cv2.VideoCapture(GENERATE_ORIGIN_VIDEO_PATH)
#     # 비디오 재생
#     frames = []
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         # 출력 비디오에 현재 프레임 쓰기
#         frames.append(frame)
#     if reverse:
#         frames = reversed(frames)

#     for frame in frames:
#         output_video.write(frame)

#     # 비디오 역재생을 위해 비디오 캡쳐 객체 초기화
#     cap.release()


# @pytest.mark.order(4)
# def test_can_reverse_generated_video():
#     # given : 유효한 비디오 파일
#     # when : 비디오 파일 역 재생 및 연결
#     # 비디오 속성 가져오기
#     reversed_video_path = VideoManager(test_img_folder_path).reverse_generated_video(GENERATE_ORIGIN_VIDEO_PATH, "reversed_video.mp4")

#     # then : 비디오 파일 유효성 확인
#     assert os.path.exists(reversed_video_path)


@pytest.mark.order(5)
def test_can_slow_generated_video():
    # given : 유효한 비디오 파일
    # when : 비디오 파일 역 재생 및 연결
    # 비디오 속성 가져오기
    slow_video_path = VideoManager(test_img_folder_path).slow_generated_video(REVERSED_VIDEO_PATH, "slow_video.mp4")

    # then : 비디오 파일 유효성 확인
    assert os.path.exists(slow_video_path)
