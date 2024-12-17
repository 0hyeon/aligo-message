import requests
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import os

app = APIRouter(prefix="/message")


@app.post("/send")
async def send_message(
    receiver: str,
    msg: str = "구매완료 테스트문자입니다.",
    msg_type: str = "SMS",
    title: str = "제목없음",
    testmode_yn: str = "N",
):
    load_dotenv()
    key = os.getenv("ALIGO_KEY")
    user_id = os.getenv("ALIGO_USER_ID")
    sender = os.getenv("ALIGO_SENDER")
    print(key, user_id, sender)
    """
    메시지를 전송합니다.
    :param key: API 인증 키
    :param user_id: 사용자 ID
    :param sender: 발신자 번호
    :param receiver: 수신자 번호 (쉼표로 구분)
    :param msg: 메시지 내용
    :param msg_type: 메시지 타입 (SMS, LMS, MMS)
    :param title: 제목 (LMS, MMS만 허용)
    :param testmode_yn: 테스트 모드 (Y/N)
    """
    api_url = "https://apis.aligo.in/send/"
    sms_data = {
        "key": key,
        "user_id": user_id,
        "sender": sender,
        "receiver": receiver,
        "msg": msg,
        "msg_type": msg_type,
        "title": title,
        "testmode_yn": testmode_yn,
    }

    try:
        response = requests.post(api_url, data=sms_data)
        print("response : ", response)
        print("response body: ", response.text)  # 응답 본문 출력
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"API Error: {response.text}",
            )
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
