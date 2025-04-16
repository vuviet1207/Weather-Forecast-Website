import pandas as pd

# Đọc file CSV
input_file = 'E:\Vlu\cachehotroraquyetdinh\DSS_Weather_Project-main\WEB_sunLight\phan_thiet.csv'  # Thay bằng đường dẫn file CSV thực tế của bạn
output_file = 'filtered_data.csv'  # Tên file đầu ra sau khi lọc

# Đọc dữ liệu từ file CSV
df = pd.read_csv(input_file)

# Danh sách các cột cần giữ lại
columns_to_keep = ['name', 'datetime', 'tempmax', 'tempmin', 'temp', 'humidity', 'precip', 'preciptype']

# Lọc các cột có trong file CSV
available_columns = [col for col in columns_to_keep if col in df.columns]
filtered_df = df[available_columns]

# Lưu dữ liệu đã lọc vào file CSV mới
filtered_df.to_csv(output_file, index=False)

print(f"Dữ liệu đã được lọc và lưu vào file: {output_file}")
print(f"Các cột được giữ lại: {available_columns}")