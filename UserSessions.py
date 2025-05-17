import json

user_sessions = {}


def load_sessions():
    try:
        with open("user_sessions.json", "rt", encoding="UTF-8") as f:
            user_sessions.update(json.load(f))
        print("Загружены сессии:", user_sessions)
    except Exception as ex:
        print("Ошибка при загрузке файла сессий:", ex)


load_sessions()


def save_sessions():
    # don't save word dictionaries
    sessions = {}
    sessions.update(user_sessions)
    for ud in sessions.values():
        if ud.get("words_dict"):
            del ud["words_dict"]
    with open("user_sessions.json", "wt", encoding="UTF-8") as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)


default_dict_name = "/dict_eng"

user_session = None


def load_session(user_id = None):
    # assume current session has been loaded
    global user_session
    if not user_id:
        return user_session

    session = user_sessions.get(str(user_id))
    if not session:
        session = {}
        session["selected_dict"] = default_dict_name
        session["correct_word"] = None
        user_sessions[str(user_id)] = session
    user_session = session
    return session


def selected_dict():
    return user_session["selected_dict"]


def words_dict():
    return user_session["words_dict"]
