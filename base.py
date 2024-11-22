import re
from whatsapp_chatbot_python import GreenAPIBot, Notification, BaseStates

bot = GreenAPIBot(
    "", ""
)

class States(BaseStates):
    MENU = "menu",
    PC_SPEC = "pc_spec",
    LAPTOP_BY_SPEC = "laptop_by_spec",
    LAB = "lab",
    SP = "sp"



@bot.router.message(text_message="start", state=None)
def message_menu_handler(notification: Notification) -> None:
    sender = notification.sender
    state = notification.state_manager.get_state(sender)
    if not state:
        notification.state_manager.set_state(sender, States.MENU.value)
        notification.answer(
        (
            "איך נוכל לעזור לך?\n"
            "1. התאמת מפרט מחשב לפי תקציב וצכרים\n"
            "2. המלצה על מחשב נייד\n"
            "3. נציג מכירות\n"
            "4. מעבדה\n"
            "הקלידו את מספר או שם שירות הרצוי"
        )                                       
    )
    else:
        notification.state_manager.delete_state(sender)
    
    


@bot.router.message(text_message=["1", "התאמת מפרט מחשב לפי תקציב וצכרים"], state=States.MENU.value)
def message_pc_by_spec_handler(notification: Notification) -> None:
    sender = notification.sender
    notification.state_manager.set_state(sender, States.PC_SPEC.value)
    notification.answer(
        (
            "על מנת להתאים את המפרט, ענו בהודעה ותפרטו עבור כל אחד מהסעיפים הבאים:\n"
            "1. מה יהיה השימוש העיקרי של המחשב?\n"
            "2. האם נדרש WIFI\BLUETOOTH מובנה?\n"
            "3. כמה נפח אחסון נדרש?\n"
            "4. האם יש חשיבות לגודל, צבע או אורות RGB במארז?\n"
            "5. האם נדרש ציוד הקפי? אם כן איזה\n"
            "6. מה מסרגת התקציב\n"
            "תשתדלו לציין כמה שיותר פרטים, כך המערכת תהיה מותאמת"
        )                                       
    )

@bot.router.message(text_message=["2", "המלצה על מחשב נייד"], state=States.MENU.value)
def message_laptop_by_spec_handler(notification: Notification) -> None:
    sender = notification.sender
    notification.state_manager.set_state(sender, States.LAPTOP_BY_SPEC.value)
    notification.answer(
        (
            "ציינו בבקשה מה יהיה השימוש של המחשב ומה התקציב שלכם"
        )                                       
    )

@bot.router.message(text_message=["3", "נציג מכירות"], state=States.MENU.value)
def message_sp_handler(notification: Notification) -> None:
    sender = notification.sender
    notification.state_manager.set_state(sender, States.SP.value)
    notification.answer(
        "איך נוכל לעזור?"
    )

@bot.router.message(text_message=["4", "מעבדה"], state=States.MENU.value)
def message_lab_handler(notification: Notification) -> None:
    sender = notification.sender
    notification.state_manager.set_state(sender, States.LAB.value)
    notification.answer(
        "איך נוכל לעזור?"
    )

@bot.router.message()
def message_respone_handler(notification: Notification) -> None:
    sender = notification.sender
    state = notification.state_manager.get_state(sender)
    if state:
        if state.name != States.MENU.value:
            notification.answer(
                "פנייתכם התקבלה, שירות לקוחות יחזור אליכם בהקדם"
            )
            notification.state_manager.delete_state(notification.sender)



bot.run_forever()