import asyncio
import json
from fastapi import FastAPI, HTTPException  # import fastapi để sử dụng trong dự án
from fastapi.middleware.cors import (
    CORSMiddleware,
)  # import thư viện cors để bỏ chặn bảo mật giữa frontend và backend
from pydantic import BaseModel
from base_code.security_info import *
from base_code.string_python_en import responses
from login_register_database import *
from base_code.get_token import generate_random_token_string
from base_code.base import *
from base_code.gettime import *
from base_code.get_token import *
from base_code.get_code import *
from login_register_database import *
from catcha_code_for_send_email import *
from email_with_python.send_emails import *
from hash_function import *


app = FastAPI()  # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    username: str
    password: str
    email: str
    islogin: bool


# chức năng login (phương anh )
@app.post("/api/login_basic")  # api login
async def login_basic(request_data: dict):  # hàm xử lý chức năng login
    if request_data:
        # print(request_data)
        # print(type(request_data))
        name_user = request_data["name"]  # nhận các tham số từ frontend
        password = request_data["pass"]

        login_check = query_database_for_login_register_by_name(
            name=name_user
        )  # truy xuất trong database bằng name truyền vào từ frontend
        login_token = generate_random_token_string(
            length=12
        )  # tạo token cho phiên đăng nhập
        if login_check:
            # id1_,name1 , email1 , password1, createdtime1 = login_check
            password1 = login_check["password"]
            email1 = login_check["email"]
            avata_img1 = login_check["avata_img"]
            # if password == password1:
            if verify_password(hex_string=password1, password=password):
                return {
                    "response": {
                        "message": responses["dang_nhap_thanh_cong"],
                        "status": True,
                        "token": login_token,
                        "email": email1,
                        "avata_img": avata_img1,
                    }
                }
            else:
                return {
                    "response": {"message": responses["sai_mat_khau"], "status": False}
                }
        else:
            return {
                "response": {
                    "message": responses["tai_khoan_chua_duoc_dang_ky"],
                    "status": False,
                }
            }


# chức năng forgot password (dương)
@app.post("/api/forgot_password_basic")  # api đăng nhập
async def forgot_password_basic(request_data: dict):  # hàm chức năng đăng nhập
    if request_data:
        email = request_data["email"]  # lấy data từ frontend
        password = request_data["pass"]

        time_now = gettime2()  # lấy time hiện tại
        check_email = query_database_for_login_register_by_email(
            email=email
        )  # truy xuất databas bằng email

        if check_email:
            code = (
                generate_random_6_digit_number()
            )  # tạo code để xác nhận cho chức năng quên mật khẩu
            # id_, name_,email_, password_,createdtime_ = check_email
            name_ = check_email["username"]
            save_data_for_confirm_code_in_table(
                email=email, code=code, createdTime=time_now, username=name_
            )  # lưu code,name và email vào catcha
            send_email_forgot_password(
                code=code, password=passwords["outlook"], to_email=email, username=name_
            )  # giử email quên mật khẩu
            return {
                "response": {
                    "message": responses["check_email_to_get_code"],
                    "status": True,
                }
            }

        else:
            return {
                "response": {
                    "message": responses["email_chua_duoc_dang_ky"],
                    "status": False,
                }
            }


# xác nhận code khi forgot password
@app.post("/api/forgot_password_confirm_code_email")
async def forgot_password_confirm_code_email(request_data: dict):
    if request_data:
        new_password = request_data["pass"]
        email = request_data["email"]
        code = request_data["code"]

        time_now = gettime2()
        print(f"time now {time_now}")
        print(type(time_now))
        # get code from catcha ( sqlite delete after 3 minutes)
        check_code = query_data_by_email_with_max_id(email=email)
        id1, username1, email1, createdTime1, code1 = check_code
        print(f"created time = {createdTime1}")
        if check_code:
            check_time = check_time_range(
                now_time=time_now, created_time=createdTime1, minute=3
            )  # true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code1 == code:
                    update_user_by_email(
                        column="password",
                        email=email,
                        value=hash_password(password=new_password),
                    )
                    # update_user_by_email(email=email,new_password=new_password,new_username=username1)
                    return {
                        "response": {
                            "message": responses["cap_nhat_mat_khau_moi_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {"message": responses["sai_code"], "status": False}
                    }
            else:
                return {
                    "response": {
                        "message": responses["code_bi_qua_thoi_gian"],
                        "status": False,
                    }
                }


# chức năng register (lâm )
@app.post("/api/register_basic")
async def register_basic(request_data: dict):
    if request_data:
        # print(f"data = {request_data} type data = {type(request_data)}")
        # Truy cập các phần riêng lẻ bằng cách sử dụng khóa
        name = request_data["name"]
        password = request_data["pass"]
        email = request_data["email"]

        time_now = gettime2()
        check_email = query_database_for_login_register_by_email(
            email=email
        )  # truy xuất dữ liệu bằng email cho chức năng đăng ký
        if check_email:
            return {
                "response": {
                    "message": responses["email_da_duoc_dang_ky"],
                    "status": False,
                }
            }
        else:
            check_username = query_database_for_login_register_by_name(
                name=name
            )  # lấy thông tin người dùng
            if check_username:
                return {
                    "response": {
                        "message": responses["user_da_ton_tai"],
                        "status": False,
                    }
                }
            else:

                # send confirm email
                code_randum = generate_random_6_digit_number()

                send_email_confirm_registration(
                    username=name,
                    code=code_randum,
                    password=passwords["outlook"],
                    to_email=email,
                )  # gửi email
                save_data_for_confirm_code_in_table(
                    createdTime=time_now, email=email, username=name, code=code_randum
                )  # lưu data vào catcha
                # asyncio.create_task(delayed_delete_confirm_code_by_email(email=email,delay_minutes=3))# chức năng này tạm thời đóng băng để thực hiện giải pháp khác ( so sánh time tạo và time truy cập)

                return {
                    "response": {
                        "message": responses["check_email_to_get_code"],
                        "status": True,
                    }
                }
                # return json.dumps(a)
    else:
        return {"response": {"message": responses["co_loi_xay_ra"], "status": False}}


# xác nhận code khi register
@app.post("/api/register_confirm_code_email")
async def register_confirm_code_email(request_data: dict):
    if request_data:
        password = request_data["pass"]
        email = request_data["email"]
        code = request_data["code"]

        time_now = gettime2()
        print(f"time now {time_now}")
        print(type(time_now))
        # get code from catcha ( sqlite delete after 3 minutes)
        check_code = query_data_by_email_with_max_id(
            email=email
        )  # hàm check code catcha
        id1, username1, email1, createdTime1, code1 = check_code
        print(f"created time = {createdTime1}")
        if check_code:
            check_time = check_time_range(
                now_time=time_now, created_time=createdTime1, minute=3
            )  # true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code1 == code:
                    save_data_for_login_register_in_table(
                        createdTime=time_now,
                        email=email,
                        password=hash_password(password=password),
                        username=username1,
                    )  # lưu thông tin
                    return {
                        "response": {
                            "message": responses["dang_ky_thanh_cong"],
                            "status": True,
                        }
                    }
                else:
                    return {
                        "response": {"message": responses["sai_code"], "status": False}
                    }
            else:
                return {
                    "response": {
                        "message": responses["code_bi_qua_thoi_gian"],
                        "status": False,
                    }
                }


# hiện thông tin người dùng (thái)
@app.post("/api/get_user_infor")
async def get_user_infor(request_data: dict):
    if request_data:
        name = request_data["name"]
        email = request_data["email"]

        data2 = query_database_for_login_register_by_email(
            email=email
        )  # lây thông tin người dùng
        # print(data2)
        # id2_ ,username2_, email2_,password2_,createdTime2_ = data2
        username2_ = data2["username"]
        avatar_img2_ = data2["avata_img"]
        # avatar_img2_ = data2.get("avatar_img")
        birthday2_ = data2["birthday"]
        email2_ = data2["email"]
        # password2_ = data2["password"]
        createdTime2_ = data2["createdTime"]

        # if avatar_img2_ is None :
        #     avatar_img2_ = ""
        # if birthday2_ is None:
        #     birthday2_ = ""
        # print(avatar_img2_)
        return {
            "response": {
                "status": True,
                "message": {
                    "username": username2_,
                    "avatar_img": avatar_img2_,
                    "birthday": birthday2_,
                    "email": email2_,
                    # "password": password2_,
                    "createdTime": createdTime2_,
                },
            }
        }


# sửa thông tin người dùng ( thái )
@app.post("/api/edit_user_infor")
async def edit_user_infor(request_data: dict):
    if request_data:
        # print(request_data)
        email_ = request_data["email"]
        username_ = request_data["username"]
        # password_ = request_data["password"]
        birthday_ = request_data["birthday"]
        avatar_img_ = request_data["avatar_img"]

        # print(username_)
        # print(password_)
        # print(birthday_)
        # print(avatar_img_)

        if email_:
            check_email = query_database_for_login_register_by_email(email=email_)
            if check_email:
                check_username = query_database_for_login_register_by_name(
                    name=username_
                )  # lấy thông tin người dùng
                update_user_by_email(
                    column="birthday", email=email_, value=birthday_
                )  # update các thông tin mới
                # update_user_by_email(
                #     column="password",
                #     email=email_,
                #     value=hash_password(password=password_),
                # )
                update_user_by_email(
                    column="avata_img", email=email_, value=avatar_img_
                )
                if check_username:
                    return {
                        "response": {
                            "message": responses["user_da_ton_tai"],
                            "status": False,
                        }
                    }
                else:
                    update_user_by_email(
                        column="username", email=email_, value=username_
                    )

                    return {
                        "response": {
                            "message": responses["sua_thong_tin_thanh_cong"],
                            "status": True,
                        }
                    }
            else:
                return {
                    "response": {
                        "message": responses["email_chua_duoc_dang_ky"],
                        "status": False,
                    }
                }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8011, workers=5, reload=True)
