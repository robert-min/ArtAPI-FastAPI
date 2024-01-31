import os
import pytest
from fastapi.testclient import TestClient
from src.apps import create_app


# TODO : 작품이 아닌 일반 사진을 넣었을 때 어떻게 처리할 것인지 고민!!

# Mock data
user_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
test_img_path = os.path.abspath(os.path.join(user_path, "test_img"))

USERID = "user1"
IMAGE_PATH = os.path.abspath(os.path.join(test_img_path, "test.jpg"))


@pytest.fixture
def client():
    app = create_app()
    client = TestClient(app)
    yield client


def test_user_can_make_generated_content(client):
    # given : 유효한 payload (header : username, file: UpladFile)
    headers = {"id": USERID}

    with open(IMAGE_PATH, "rb") as f:
        files = {"file": ("image.jpg", f, "image/jpeg")}

        # when : 콘텐츠 생성 API 요청
        response = client.post(
            "/user/content",
            headers=headers,
            files=files)

    # then : 정상 응답 username
    assert response.status_code == 200
    assert response.json()["meta"]["message"] == "ok"
    assert response.json()["data"]["id"] == USERID


def test_user_cannot_make_generated_content_with_non_header(client):
    # given : 유효하지 않은 payload (header 없이 요청)
    # when : 콘텐츠 생성 API 요청
    with open(IMAGE_PATH, "rb") as f:
        files = {"file": ("image.jpg", f, "image/jpeg")}

        # when : 콘텐츠 생성 API 요청
        response = client.post(
            "/user/content",
            files=files)
    assert response.status_code == 422
    assert response.json()["meta"]["message"] == "A required value is missing. Please check."


def test_user_cannot_make_generated_content_with_non_file(client):
    # given : 유효하지 않은 payload (file 없이 요청)
    headers = {"id": USERID}

    # when : 콘텐츠 생성 API 요청
    response = client.post(
        "/user/content",
        headers=headers)

    # given : 에러메시지
    assert response.status_code == 422
    assert response.json()["meta"]["message"] == "A required value is missing. Please check."