from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram.ext import CallbackContext

async def welcome(update: Update, context: CallbackContext):
    # دریافت اطلاعات اعضای جدید
    new_members = update.message.new_chat_members
    for member in new_members:
        # ارسال پیام خوش‌آمدگویی
        await update.message.reply_text(f"Welcome {member.full_name}! Invite your friends to join us!")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I will welcome new users in the group.")

def main():
    application = Application.builder().token('8137611209:AAE-KVSrchV9hX5w0FVr70FZNbWiPsuxma0').build()

    # تنظیم handler برای خوش‌آمدگویی به کاربران جدید
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    # تنظیم handler برای فرمان /start
    application.add_handler(CommandHandler('start', start))

    application.run_polling()

if __name__ == '__main__':
    main()
