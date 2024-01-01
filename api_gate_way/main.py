import asyncio
import json
from fastapi import FastAPI, HTTPException # import fastapi để sử dụng trong dự án
from fastapi.middleware.cors import CORSMiddleware # import thư viện cors để bỏ chặn bảo mật giữa frontend và backend
from pydantic import BaseModel
import requests
from setting import url_host

app = FastAPI() # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# @app.post("/api/user_services")
# async def user_services():
#     pass

@app.post("/api/user_services/{service_name}")
async def user_services(service_name: str):
    response = requests.post(f"{url_host}api//users")
    return response.json()
    

@app.post("/api/tour_services")
async def tour_services():
    pass

@app.post("/api/payment_services")
async def payment_services():
    pass

# chức năng login 
@app.post("/api/login_basic")
async def login_basic(request_data: dict):
    if request_data:
        # print(request_data)
        # print(type(request_data))
        # print(f"{url_host['user_services']}api/login_basic")
        # Xử lý request_data theo nhu cầu của bạn
        # Sau đó gửi yêu cầu đến service tương ứng thông qua requests
        response = requests.post(f"{url_host['user_services']}api/login_basic", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@app.post("/api/forgot_password_basic") # api đăng nhập
async def forgot_password_basic(request_data: dict): # hàm chức năng đăng nhập
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/forgot_password_basic", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


        
# xác nhận code khi forgot password
@app.post("/api/forgot_password_confirm_code_email")
async def forgot_password_confirm_code_email(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/forgot_password_confirm_code_email", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


# chức năng register
@app.post("/api/register_basic")
async def register_basic(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/register_basic", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


# xác nhận code khi register
@app.post("/api/register_confirm_code_email")
async def register_confirm_code_email(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/register_confirm_code_email", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

# hiện thông tin người dùng 
@app.post("/api/get_user_infor")
async def get_user_infor(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/get_user_infor", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

# sửa thông tin người dùng
@app.post("/api/edit_user_infor")
async def edit_user_infor(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['user_services']}api/edit_user_infor", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)



# hiển thị tour trên trang chính
@app.get("/api/get_tourist_destination_information")
async def get_tourist_destination_information():
    response = requests.get(f"{url_host['tour_services']}api/get_tourist_destination_information")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


# hiện thông tin tour chi tiết 
@app.post("/api/get_tourist_destination_information_by_name")
async def tourist_destination_information_by_name(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['tour_services']}api/get_tourist_destination_information_by_name", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)



# chức năng offer hotel đăng hoàn thiện       
@app.post("/api/get_offer_data")
async def get_offer_data(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['tour_services']}api/get_offer_data", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
 

# @app.post("/api/the_blog")
# async def the_blog(request_data: dict):
#     if request_data:
#         pass

@app.post("/api/booking_tour")
async def booking_tour(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['tour_services']}api/booking_tour", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


@app.post("/api/my_booking_tour")
async def my_booking_tour(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['tour_services']}api/my_booking_tour", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

@app.post("/api/delete_my_booking_tour")
async def delete_my_booking_tour(request_data: dict):
    if request_data:
        response = requests.post(f"{url_host['tour_services']}api/delete_my_booking_tour", json=request_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/api/show_all_tour")
async def show_all_tour():
    response = requests.get(f"{url_host['tour_services']}api/show_all_tour")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8010, workers=5, reload=True)