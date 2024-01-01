import sqlite3
from base_code.gettime import gettime3

# xem các bảng của 1 database
def check_table_in_database(path_to_database):
    # Kết nối đến CSDL SQLite
    conn = sqlite3.connect(path_to_database)

    # Tạo con trỏ
    cursor = conn.cursor()

    # Thực thi câu truy vấn để lấy danh sách bảng
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Lấy kết quả từ câu truy vấn
    tables = cursor.fetchall()

    # In số bảng có trong CSDL
    print("Số bảng trong CSDL:", len(tables))


    # Đóng kết nối và con trỏ
    cursor.close()
    conn.close()

    return tables

# cấu trúc của bảng
def structure_of_the_table(path_to_database,table_name):
    # Kết nối đến CSDL SQLite
    conn = sqlite3.connect(path_to_database)

    # Tạo con trỏ
    cursor = conn.cursor()

    # Tên bảng cần in cấu trúc
    # table_name = 'your_table_name'

    # Thực thi câu truy vấn để lấy thông tin cấu trúc của bảng
    cursor.execute(f"PRAGMA table_info({table_name})")

    # Lấy kết quả từ câu truy vấn
    table_structure = cursor.fetchall()

    # In cấu trúc của bảng
    # print("Cấu trúc của bảng", table_name)
    # for column in table_structure:
    #     print(column)

    # Đóng kết nối và con trỏ
    cursor.close()
    conn.close()

    return table_structure

def get_max_id_from_table(path_of_database,table_name):
    conn = sqlite3.connect(path_of_database)  # Thay 'database.db' bằng đường dẫn đến tệp SQLite của bạn
    cursor = conn.cursor()
    
    query = f"SELECT MAX(id) FROM {table_name}"
    cursor.execute(query)
    
    max_id = cursor.fetchone()[0]
    
    conn.close()
    
    return max_id

# print(check_table_in_database(path_to_database="database\\tourist_destination_information.db"))

# print(structure_of_the_table(path_to_database="database\\tourist_destination_information.db",table_name="tourist_destination_information_basic_for_get_data2"))


# a = structure_of_the_table(path_to_database="database\offer.db",table_name="offer_basic")

# print(a)

def check_table_existence(database_name, table_name):
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Kiểm tra xem bảng có tồn tại hay không
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table_exists = cursor.fetchone() is not None

    # Đóng kết nối và trả về kết quả kiểm tra
    cursor.close()
    conn.close()
    return table_exists

# max_id = get_max_id_from_table(path_of_database="database\\tourist_destination_information.db",table_name="tourist_destination_information_basic_for_get_data2")
# print(max_id)
# print(check_table_existence(database_name="database\\visual_hotels_and_restaurent.db",table_name=f"visual_hotels_and_restaurent_{gettime3()}"))

# max_id = get_max_id_from_table(path_of_database="database\offer.db",table_name="offer_basic")
# print(max_id)
