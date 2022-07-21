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
}

answers = {k:{k2:symbolize(v2) for k2,v2 in v.items()} for k,v in answers.items()}