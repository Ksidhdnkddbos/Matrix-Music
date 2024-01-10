import math

from pyrogram.types import InlineKeyboardButton

from MatrixMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton(text=_["MATRIX_BUTTON"], url=f"https://t.me/XMATTMX")],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 10 < umm < 20:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 20 <= umm < 30:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 30 <= umm < 40:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 40 <= umm < 50:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 50 <= umm < 60:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 60 <= umm < 70:
        bar = "▇▅▂▅▃▄▃▁▃"
    elif 70 <= umm < 80:
        bar = "▃▇▂▅▁▅▄▃▁"
    elif 80 <= umm < 95:
        bar = "▅▄▇▂▅▂▄▇▁"
    else:
        bar = "▃▅▂▅▃▇▄▅▃"
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["MATRIX_BUTTON"], url=f"https://t.me/XMATTMX")],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="‹ تشغيل ›", callback_data=f"ADMIN Resume|{chat_id}"
            ), 
                    ],
        [
            InlineKeyboardButton(text="‹ توقف ›", callback_data=f"ADMIN Pause|{chat_id}"
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ إعادة التشغيل ›", callback_data=f"ADMIN Replay|{chat_id}"
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ تخطي ›", callback_data=f"ADMIN Skip|{chat_id}"
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ ايقاف ›", callback_data=f"ADMIN Stop|{chat_id}"
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ كتم ›", callback_data=f"ADMIN Mute|{chat_id}"                       
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ الغاء الكتم ›",callback_data=f"ADMIN Unmute|{chat_id}"
            ),
                    ],
        [

            InlineKeyboardButton(text="‹ خلط ›",callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ تكرار ›", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="‹ يمين ›",callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ رجوع ›",callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
                    ],
        [
            InlineKeyboardButton(text="‹ يسار ›",callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
        ],
        [InlineKeyboardButton(text=_["MATRIX_BUTTON"], url=f"https://t.me/XMATTMX")],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"Playlists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"Playlists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton(text=_["MATRIX_BUTTON"], url=f"https://t.me/XMATTMX")],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [InlineKeyboardButton(text=_["MATRIX_BUTTON"], url=f"https://t.me/XMATTMX")],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons



def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ ارجاع 10ث ›",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="‹ تقديم 10ث ›",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="‹ ارجاع 30ث ›",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="‹ تقديم 30ث ›",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="يمين",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="‹ رجوع ›",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="يسار",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons
