#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Bot Standalone Server
Botni alohida ishga tushirish uchun
"""
import sys
import os
import asyncio
import logging
from pathlib import Path

# Loyiha ildizini sys.path ga qo'shish
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Environment variables yuklash
from dotenv import load_dotenv
load_dotenv()

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Botni ishga tushirish"""
    try:
        # Flask app va db ni import qilish
        from app import app, db
        from telegram_bot import create_telegram_app
        from debt_scheduler import init_debt_scheduler
        
        logger.info("🤖 Telegram Bot ishga tushirilmoqda...")
        
        # Scheduler ni ishga tushirish
        logger.info("📅 Scheduler ishga tushirilmoqda...")
        scheduler = init_debt_scheduler(app, db)
        
        # Telegram application yaratish
        logger.info("📱 Telegram application yaratilmoqda...")
        application = create_telegram_app()
        
        if not application:
            logger.error("❌ Telegram application yaratilmadi!")
            return
        
        logger.info("✅ Telegram Bot tayyor!")
        logger.info("📞 Bot manzili: https://t.me/UzunHissobot_bot")
        logger.info("🔄 Bot polling rejimida ishlamoqda...")
        
        # Bot polling rejimida ishga tushirish
        application.run_polling(
            allowed_updates=["message", "callback_query", "inline_query"]
        )
        
    except KeyboardInterrupt:
        logger.info("\n⛔ Bot to'xtatildi (Ctrl+C)")
        if 'scheduler' in locals():
            scheduler.stop()
    except Exception as e:
        logger.error(f"❌ Xatolik: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
