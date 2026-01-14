from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

# 🔐 READ TOKEN FROM FILE (Replit safe method)
with open("secret.txt", "r") as f:
    TOKEN = f.read().strip()

# ======================
# MAIN MENU
# ======================
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📌 Services", callback_data="menu_services")],
        [InlineKeyboardButton("💰 Pricing", callback_data="menu_pricing")],
        [InlineKeyboardButton("📞 Contact", callback_data="menu_contact")],
        [InlineKeyboardButton("❓ Help", callback_data="menu_help")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ======================
# SERVICES MENU
# ======================
def services_menu():
    keyboard = [
        [
            InlineKeyboardButton("🌐 Website", callback_data="service_web"),
            InlineKeyboardButton("🖥 Software", callback_data="service_software"),
        ],
        [
            InlineKeyboardButton("📱 Mobile Apps", callback_data="service_mobile"),
            InlineKeyboardButton("🎨 Design", callback_data="service_design"),
        ],
        [
            InlineKeyboardButton("⌨️ Typing", callback_data="service_typing"),
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="back_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


# ======================
# START COMMAND
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to *Rozh Studio*\n\n"
        "Professional digital services.\n"
        "Choose an option below:",
        reply_markup=main_menu(),
        parse_mode="Markdown",
    )


# ======================
# BUTTON HANDLER
# ======================
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # ----- MAIN MENU -----
    if data == "menu_services":
        await query.edit_message_text(
            "📌 *Rozh Studio Services*\nSelect a service:",
            reply_markup=services_menu(),
            parse_mode="Markdown",
        )

    elif data == "menu_pricing":
        await query.edit_message_text(
            "💰 *Pricing & Packages*\n\n"
            "✔ Prices depend on project size\n"
            "✔ Affordable & flexible\n\n"
            "Contact us for a custom quote.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="back_main")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "menu_contact":
        await query.edit_message_text(
            "📞 *Contact Rozh Studio*\n\n"
            "📧 Email: rozhstudio@email.com\n"
            "📱 Telegram: @RozhStudio\n\n"
            "We respond quickly!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="back_main")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "menu_help":
        await query.edit_message_text(
            "❓ *Help*\n\n"
            "• Use the buttons to navigate\n"
            "• Choose services easily\n"
            "• Contact us anytime",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="back_main")]]
            ),
            parse_mode="Markdown",
        )

    # ----- SERVICES -----
    elif data == "service_web":
        await query.edit_message_text(
            "🌐 *Website Development*\n\n"
            "✔ Modern design\n"
            "✔ Fast & responsive\n"
            "✔ SEO ready",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="menu_services")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "service_software":
        await query.edit_message_text(
            "🖥 *Custom Software*\n\n"
            "✔ Desktop apps\n"
            "✔ Business automation\n"
            "✔ Custom solutions",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="menu_services")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "service_mobile":
        await query.edit_message_text(
            "📱 *Mobile App Development*\n\n"
            "✔ Android & iOS\n"
            "✔ High performance\n"
            "✔ Clean UI/UX",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="menu_services")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "service_design":
        await query.edit_message_text(
            "🎨 *UI/UX & Graphic Design*\n\n"
            "✔ Modern layouts\n"
            "✔ Branding & visuals\n"
            "✔ Professional look",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="menu_services")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "service_typing":
        await query.edit_message_text(
            "⌨️ *Typing & Data Entry*\n\n"
            "✔ Fast typing\n"
            "✔ Accurate documents\n"
            "✔ Formatting services",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="menu_services")]]
            ),
            parse_mode="Markdown",
        )

    elif data == "back_main":
        await query.edit_message_text(
            "🏠 *Main Menu*\nChoose an option:",
            reply_markup=main_menu(),
            parse_mode="Markdown",
        )


# ======================
# APP SETUP
# ======================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("🤖 Rozh Studio Bot is running")
app.run_polling()
