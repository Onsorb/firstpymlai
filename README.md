این اسکریپت یک تحلیل ساده و تصویری داده‌ها با استفاده از Pandas و Matplotlib انجام می‌دهد. هدف آن نشان دادن نحوه پردازش داده‌ها و نمایش چند نوع نمودار پیشرفته در یک صفحه است.
🔹 ویژگی‌های اصلی کد
ساخت DataFrame با Pandas
داده‌های نمونه شامل اطلاعات مشتریان، سن، شهر، تعداد خرید و قیمت خرید هستند.
Pandas برای مدیریت جدول داده‌ها استفاده می‌شود و عملیات فیلتر، گروه‌بندی و محاسبات آماری روی آن انجام می‌شود.
تحلیل داده‌ها
نمودار ستونی برای نمایش تعداد خرید هر مشتری
نمودار دایره‌ای برای نشان دادن سهم فروش هر شهر
نمودار خطی برای نمایش روند قیمت خرید مشتریان
نمودار پراکندگی (Scatter) برای بررسی رابطه تعداد خرید و قیمت
نمایش چند نمودار همزمان
از plt.subplots استفاده شده تا چهار نمودار در یک صفحه رسم شوند.
هر نمودار به یک subplot اختصاص دارد و با tight_layout() فاصله بین نمودارها بهینه شده است.
ویژگی‌های پیشرفته بصری
رنگ‌بندی مختلف برای هر نمودار
استفاده از مارکر و linestyle در نمودار خطی
اندازه نقاط در نمودار پراکندگی قابل تنظیم است
🔹 کاربردها
آموزش مقدماتی Pandas و Matplotlib برای تحلیل داده‌ها
تمرین کار با DataFrame و گروه‌بندی داده‌ها
نمایش تصویری داده‌ها و مقایسه آن‌ها
آماده‌سازی برای پروژه‌های Data Analysis و Data Visualization

Data Analysis & Visualization with Pandas and Matplotlib
This script demonstrates data analysis and visualization using Python's Pandas and Matplotlib libraries. It creates a sample dataset of customers and their purchases and displays multiple types of charts in a single figure.
Features
DataFrame Management: Handles customer data including age, city, purchase count, and price.
Data Analysis:
Bar chart for number of purchases per customer
Pie chart for sales share by city
Line chart for purchase price trend
Scatter plot for relationship between purchase count and price
Advanced Visualization: Uses subplots to display multiple charts together with customized colors, markers, and styles.
Flexible & Extendable: Can easily be adapted to real CSV datasets for practical analysis.
Use Cases
Learning Pandas and Matplotlib for data handling and visualization
Practicing data grouping, filtering, and statistical analysis
Creating visual reports and dashboards for small datasets
