keywords = [[2, 'en', 'fa', 'انگلیسی', 'فارسی'], [
    3, 'all', 'custom', 'off', 'همه', 'شخصی سازی شده', 'خاموش'], [
    9, 'typing', 'playing', 'upload_photo', 'record_video', 'record_voice', 'upload_document', 'choose_sticker', 'find_location', 'record_video_note',
    'تایپینگ', 'بازی کردن', 'ارسال عکس', 'ارسال ویدئو', 'ارسال ویس', 'ارسال فایل', 'انتخاب استیکر', 'پیدا کردن لوکیشن', 'ارسال ویدئو نوت'
    ]]


def get_farsi(keyword):
    for k in keywords:
        if keyword in k:
            count = k[0]
            index = k.index(keyword) - 1
            return k[(1 + count):][index]
    return None


def get_by_language(keyword, language):
    if language == 'fa':
        return get_farsi(keyword)
    else:
        return keyword
