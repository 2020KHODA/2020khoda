# 🚀 مجموعه پروژه‌های خفن ۲۰۲۰خدا

دمو آنلاین:  
📺 [مشاهده در GitHub Pages](https://2020khoda.github.io/)

---

این ریپو شامل سه نمونه پروژه برای نمایش قدرت زبان‌های مختلف برنامه‌نویسیه.  
هر پروژه توی پوشه خودش قرار داره و جداگانه قابل ران شدنه.  

---

## 📌 1. Python Async Scraper
- استفاده از `asyncio` + `aiohttp` برای درخواست‌های همزمان.  
- مدیریت **Rate Limit**, **Retry** با **Backoff** و **Caching**.  

📂 مسیر: `python-async-scraper/`

---

## 📌 2. Rust Rayon Demo
- استفاده از **Rayon** برای پردازش موازی (Parallel Processing).  
- مثال: جمع‌کردن آرایه بزرگ با سرعت بالا.  

📂 مسیر: `rust-rayon-demo/`

---

## 📌 3. ۲۰۲۰خدا (Galaxy Canvas)
- پروژه هنری/نمایشی با **HTML + CSS + JavaScript**  
- نمایش انیمیشن ستاره‌ها روی بوم (Canvas).  

📂 مسیر: `galaxy-canvas/`

📷 پیش‌نمایش:  
![Galaxy Demo](docs/galaxy-demo.png)

---

## 💡 نحوه اجرا
### Python Scraper:
```bash
cd python-async-scraper
pip install -r requirements.txt
python scraper.py
