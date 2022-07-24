from base.utils import symbolize

answers = {
    'ping': {
        'en': 'I am online !',
        'fa': 'ربات آنلاین است !'
    },
    'set_language_already': {
        'en': 'Language is {} already !',
        'fa': 'زبان از قبل {} بوده است !'
    },
    'language_changed': {
        'en': 'Language changed to {} !',
        'fa': 'زبان ربات به {} تغییر کرد !'
    },
    'start_downloading': {
        'en': 'Downloading started ...',
        'fa': 'دانلود مدیا شروع شد ...'
    },
    'downloaded': {
        'en': 'Media successfully saved in your saved messages !',
        'fa': 'مدیا با موفقیت در سیو مسیج های شما ذخیره شد !'
    },
    'reply_on_media': {
        'en': 'Reply on media !',
        'fa': 'لطفا روی مدیا مورد نظر reply کنید !'
    },
    'dice': {
        'en': 'Required number is {}!',
        'fa': 'عدد مورد نظر {} است!'
    },
    'dart': {
        'en': 'The Dart Hit The Target!',
        'fa': 'دارت به هدف خورد!'
    },
    'check_update': {
        'en': 'please wait...',
        'fa': 'لطفا صبر کنید...'
    },
    'update': {
        'en': 'The bot has been successfully updated.',
        'fa': "ربات با موفقیت اپدیت شد."
    },
    'already_update': {
        'en': 'There is no new update available!',
        'fa': "اپدیت جدیدی در دسترس نمیباشد!"
    },
    'already_action_mode': {
        'en': 'Action mode already is \"{}\" !',
        'fa': 'حالت ارسال اکشن در حال حاضر \"{}\" است !'
    },
    'action_mode_setted': {
        'en': 'Action mode setted to \"{}\" !',
        'fa': 'حالت ارسال اکشن به روی \"{}\" تنظیم شد.'
    },
    'already_action_type': {
        'en': 'Action type already is \"{}\" !',
        'fa': 'نوع اکشن در حال حاضر \"{}\" است !'
    },
    'action_type_setted': {
        'en': 'Action type setted to \"{}\" !',
        'fa': 'نوع اکشن به روی \"{}\" تنظیم شد !'
    },
    'added_to_action_chats': {
        'en': 'This chat added to action chats !',
        'fa': 'این چت به لیست ارسال اکشن اضافه شد !'
    },
    'already_added_to_action_chats': {
        'en': 'This chat already is in action chats !',
        'fa': 'این چت در حال حاضر در لیست ارسال اکشن وجود دارد !'
    },
    'removed_from_action_chats': {
        'en': 'This chat removed from action chats !',
        'fa': 'این چت از لیست ارسال اکشن حذف شد !'
    },
    'already_removed_from_action_chats': {
        'en': 'This chat already not exist in action chats !',
        'fa': 'این چت در حال حاضر در لیست ارسال اکشن وجود ندارد !'
    }
}

answers = {k:{k2:symbolize(v2) for k2,v2 in v.items()} for k,v in answers.items()}