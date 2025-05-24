import dict_general
import dict_econ
import dict_pdb


dict_list = {
    "English General": ("/dict_eng", dict_general.words_dict),
    "English Economics": ("/dict_enec", dict_econ.words_dict),
    "Python Databases": ("/dict_pdb", dict_pdb.words_dict),
}


def dict_info(selected_dict):
    info_list = []
    for name in dict_list:
        command, dict = dict_list[name]
        sel_icon = "✅" if selected_dict == command else "☑️"
        info_list.append(f"{sel_icon} {command} - {name} ({len(dict)} слов)")
    return "\n".join(info_list)


def load_dict(command):
    print("Загрузка словаря", command)
    name, dict = next(
        ((k, d) for k, (cmd, d) in dict_list.items() if cmd == command), None
    )
    return name, dict

