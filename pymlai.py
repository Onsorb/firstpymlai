import pandas as pd
import matplotlib.pyplot as plt

# دیتای نمونه
data = {
    "Customer": ["Ali", "Fatemeh", "Reza", "Niloofar", "Mina"],
    "Age": [25, 34, 29, 42, 22],
    "City": ["Tehran", "Mashhad", "Tehran", "Shiraz", "Mashhad"],
    "Purchase": [3, 5, 2, 7, 1],
    "Price": [250, 800, 120, 1500, 300]
}

df = pd.DataFrame(data)

# ساخت figure با 2 ردیف و 2 ستون
fig, axs = plt.subplots(2, 2, figsize=(14,10))

# 1. نمودار ستونی تعداد خرید هر مشتری
df.plot(x="Customer", y="Purchase", kind="bar", ax=axs[0,0], color="skyblue")
axs[0,0].set_title("تعداد خرید هر مشتری")
axs[0,0].set_ylabel("تعداد خرید")

# 2. نمودار دایره‌ای مجموع خرید بر اساس شهر
city_sales = df.groupby("City")["Price"].sum()
city_sales.plot(kind="pie", autopct='%1.1f%%', ax=axs[0,1], startangle=90)
axs[0,1].set_title("سهم فروش هر شهر")
axs[0,1].set_ylabel("")

# 3. نمودار خطی روند قیمت خرید مشتریان
df.plot(x="Customer", y="Price", kind="line", ax=axs[1,0], marker='o', linestyle='--', color="green")
axs[1,0].set_title("روند قیمت خرید مشتریان")
axs[1,0].set_ylabel("قیمت")

# 4. نمودار پراکندگی (Scatter) تعداد خرید در مقابل قیمت
df.plot.scatter(x="Purchase", y="Price", ax=axs[1,1], color="red", s=100)
axs[1,1].set_title("تعداد خرید vs قیمت")

# مرتب کردن فاصله‌ها
plt.tight_layout()
plt.show()
