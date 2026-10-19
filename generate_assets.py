#!/usr/bin/env python3
"""تولید QR Code با وضوح بالا (300 DPI) و تصحیح خطای حداکثری (H) برای چاپ جعبه و لیبل کیک و شیرینی ریلیا."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import PIL  # noqa: F401
except ImportError:
    print(
        "کتابخانه Pillow یافت نشد. دستور زیر را اجرا کنید:\n"
        'pip install "qrcode[pil]"',
        file=sys.stderr,
    )
    raise SystemExit(1)

import qrcode
from pydantic import BaseModel, Field, HttpUrl, field_validator
from qrcode.constants import ERROR_CORRECT_H

# آدرس نهایی GitHub Pages اختصاصی شما
DEFAULT_PRODUCTION_URL = "https://neganinshell.github.io/riliacake/"


class QRCodeConfig(BaseModel):
    landing_url: HttpUrl = Field(
        ...,
        description="آدرس صفحه فرود که درون کد QR ذخیره می‌شود.",
    )
    box_size: int = Field(
        default=24,
        ge=8,
        le=64,
        description="ابعاد هر ماژول کیوآرکد به پیکسل (چاپ باکیفیت بالا).",
    )
    border: int = Field(
        default=4,
        ge=2,
        le=12,
        description="حاشیه سفید اطراف کیوآرکد (Quiet Zone).",
    )
    fill_color: str = Field(default="#1a1a1a", description="رنگ پترن اصلی.")
    back_color: str = Field(default="#ffffff", description="رنگ پس‌زمینه.")

    @field_validator("landing_url")
    @classmethod
    def validate_url(cls, value: HttpUrl) -> HttpUrl:
        if not value.host:
            raise ValueError("آدرس اینترنتی باید دامنه معتبر داشته باشد.")
        return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="تولید بارکد QR اختصاصی صفحه فرود Riliacake با کیفیت افست."
    )
    parser.add_argument(
        "url_pos",
        metavar="URL",
        nargs="?",
        default=None,
        help="آدرس اینترنتی (اختیاری؛ در صورت خالی بودن از URL پروداکشن استفاده می‌شود).",
    )
    parser.add_argument(
        "--url",
        dest="url_flag",
        default=None,
        help="آدرس اینترنتی جایگزین.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="print_ready_qr.png",
        help="نام فایل خروجی تصویر (پیش‌فرض: print_ready_qr.png).",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    raw_url = args.url_flag or args.url_pos or DEFAULT_PRODUCTION_URL

    try:
        config = QRCodeConfig(landing_url=raw_url)
    except Exception as exc:
        print(f"[خطا در اعتبارسنجی ورودی]: {exc}", file=sys.stderr)
        return 1

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=config.box_size,
        border=config.border,
    )
    qr.add_data(str(config.landing_url))
    qr.make(fit=True)

    img = qr.make_image(fill_color=config.fill_color, back_color=config.back_color)

    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = Path.cwd() / out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, format="PNG", dpi=(300, 300))

    print(f"✔ فایل کیوآرکد با موفقیت ساخته شد: {out_path.name}")
    print(f"✔ آدرس کدگذاری‌شده: {config.landing_url}")
    print(
        f"✔ تنظیمات چاپ: 300 DPI | سطح خطای H | اندازه ماژول: {config.box_size}px"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())