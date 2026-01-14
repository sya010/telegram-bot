from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# ✅ Get the token from environment variables (safe for GitHub)
TOKEN = os.environ.get("BOT_TOKEN")

# --- Command functions ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Rozh Studio Bot! Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/services - View Rozh Studio services\n"
        "/coding - Website, software, app info\n"
        "/web - Website design & development\n"
        "/software - Custom software development\n"
        "/mobile - Mobile app development\n"
        "/design - UI/UX & graphic design\n"
        "/typing - Typing, data entry & documents\n"
        "/pricing - Pricing & packages\n"
        "/contact - Contact or request project\n"
        "/help - Show this help menu"
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Rozh Studio Services:\n"
        "Website, Software, Mobile Apps, UI/UX Design, Typing/Data Entry"
    )

async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💻 Rozh Studio can create websites, software, and mobile apps."
    )

async def web(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Website services: design, development, SEO-friendly, responsive."
    )

async def software(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖥️ Custom software: desktop apps, automation, and business solutions."
    )

async def mobile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Mobile apps for Android & iOS with high-quality UI/UX."
    )

async def design(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 Graphic & UI/UX design: modern, creative, and professional."
    )

async def typing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⌨️ Typing, data entry, document formatting, and admin support."
    )

async def pricing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Ask about pricing and packages via /contact or message us."
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Contact Rozh Studio: [Your email/phone] or DM here."
    )

# --- Set up the bot ---
app = ApplicationBuilder().token(TOKEN).build()

# Add all command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("services", services))
app.add_handler(CommandHandler("coding", coding))
app.add_handler(CommandHandler("web", web))
app.add_handler(CommandHandler("software", software))
app.add_handler(CommandHandler("mobile", mobile))
app.add_handler(CommandHandler("design", design))
app.add_handler(CommandHandler("typing", typing))
app.add_handler(CommandHandler("pricing", pricing))
app.add_handler(CommandHandler("contact", contact))

print("🤖 Rozh Studio Bot started")
app.run_polling()
