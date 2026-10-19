# کیک و شیرینی ریلیا (Riliacake) — Landing Page

لندینگ پیج استاتیک لینک‌ها + QR Code آماده چاپ برای برند **Riliacake**، میزبانی شده روی GitHub Pages (بدون سرور، بدون هزینه).

## فایل‌ها

- `index.html` — لندینگ پیج تک‌فایلی (RTL، واکنش‌گرا، موبایل‌فرندلی)
- `generate_assets.py` — تولید `print_ready_qr.png` با بالاترین سطح تصحیح خطا (H)
- `Pydantic.py` — اعتبارسنجی داده‌های تماس برند با Pydantic

## تولید QR Code

پیش‌نیاز: `qrcode` و `pydantic` (و Pillow برای خروجی PNG).

```bash
pip install "qrcode[pil]" pydantic
```

قبل از چاپ، آدرس GitHub Pages خود را جایگزین کنید:

```bash
python generate_assets.py --url https://YOUR_USERNAME.github.io/YOUR_REPO/
```

یا مستقیم:

```bash
python generate_assets.py "https://YOUR_USERNAME.github.io/YOUR_REPO/"
```

خروجی: `print_ready_qr.png` با وضوح بالا (DPI 300) و تصحیح خطای سطح H.

## دستورالعمل استقرار (Deployment Guide) — ۳ مرحله

### مرحله ۱: ایجاد ریپازیتوری و Push کردن کد

```bash
cd /path/to/reyhaneh
git init
git add .
git commit -m "feat: add Riliacake landing page and QR generator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### مرحله ۲: فعال‌سازی GitHub Pages

1. به صفحه ریپازیتوری در GitHub بروید.
2. از منوی بالا **Settings** را انتخاب کنید.
3. از سایدبار سمت چپ **Pages** را انتخاب کنید.
4. در بخش **Build and deployment**:
   - **Source**: گزینه **Deploy from a branch** را انتخاب کنید.
   - **Branch**: شاخه `main` و پوشه `/ (root)` را انتخاب کنید.
   - روی **Save** کلیک کنید.
5. پس از چند ثانیه/دقیقه، آدرس سایت شما در همان صفحه نمایش داده می‌شود:
   `https://YOUR_USERNAME.github.io/YOUR_REPO/`

### مرحله ۳: به‌روزرسانی QR Code و چاپ

1. آدرس نهایی GitHub Pages را کپی کنید.
2. QR Code جدید را تولید کنید:
   ```bash
   python generate_assets.py --url https://YOUR_USERNAME.github.io/YOUR_REPO/
   ```
3. فایل `print_ready_qr.png` را با وضوح ۳۰۰ DPI روی برچسب/جعبه چاپ کنید.

> نکته: چون QR با سطح تصحیح H تولید شده، حتی در صورت خراشیدگی جزئی روی جعبه هم قابل اسکن خواهد بود.
# riliacake
