import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackContext
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

async def welcome(update: Update, context: CallbackContext):
    # دریافت اطلاعات اعضای جدید
    new_members = update.message.new_chat_members
    for member in new_members:
        # اطمینان از موجود بودن نام کامل کاربر
        full_name = f"{member.first_name} {member.last_name}" if member.last_name else member.first_name
        # ارسال پیام خوش‌آمدگویی
        await update.message.reply_text(f"Welcome {full_name}! Invite your friends to join us!")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am completely free, and you can add me to your group!")

def main():
    # بارگذاری توکن از متغیر محیطی
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise ValueError("No token found! Please set the TELEGRAM_TOKEN environment variable.")
    
    application = Application.builder().token(token).build()

    # تنظیم handler برای خوش‌آمدگویی به کاربران جدید
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    # تنظیم handler برای فرمان /start
    application.add_handler(CommandHandler('start', start))

    # استفاده از webhook
    application.run_webhook(
        listen="0.0.0.0",  # برای دسترسی عمومی (مناسب برای Render)
        port=int(os.getenv("PORT", 8080)),  # از پورت 8080 یا پورت تنظیمی Render استفاده کنید
        url_path=token,  # مسیر URL برای webhook
        webhook_url=f"https://fun-r5xc.onrender.com/{token}"  # URL کامل webhook برای سرویس Render
    )

if __name__ == '__main__':
    main()
