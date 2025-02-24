import csv
from datetime import datetime, timedelta


def get_log(filepath):
    with open(filepath , 'r') as file:
        ml_logs = list(csv.reader(file))    # mnogu poprofi e vaka
    return ml_logs     # koj rezultat da go vrati taa funckija


def write_log(ml_arg, filepath):
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ml_arg)


# ----------  FEED  -----------
# prikaz na sekoe hranenje
def get_ml_log_str(ml_log):
    ml_log_str = ''
    for meal in ml_log:
        # meal = list(meal)
        # st.write(meal)
        meal_edit = f"{meal[0]} - {meal[1]} ml - {meal[2]} - {meal[3]}\n"
        ml_log_str = ml_log_str + meal_edit
    return ml_log_str


# konvertiranje na ml_log od DIC vo STR za print na dneven total
def get_ml_str(total_dic):
    result_ml = ''
    for key_dose in total_dic:
        result_ml = result_ml + (f"{key_dose}   =   "
                                 f"{total_dic[key_dose][0] + total_dic[key_dose][1]} ml"
                                 f"   =   M: {total_dic[key_dose][0]} ml"
                                 f"   +   F: {total_dic[key_dose][1]} ml\n")
    return result_ml


# obrabotka na ml_log vo lista na total ispieno vo den:
def get_total_ml(ml_log):
    ml_log_dic = {}
    for feed in ml_log:
        key = str(feed[3])
        if key not in ml_log_dic:
            ml_log_dic[key] = [0,0]
        milk_type = feed[2]
        add_ml = int(feed[1])
        match milk_type:
            case "Mama's":
                ml_log_dic[key][0] += add_ml
            case "Formula":
                ml_log_dic[key][1] += add_ml
    sorted_dict_asc = {k: ml_log_dic[k] for k in sorted(ml_log_dic, reverse=True)}
    return sorted_dict_asc


# ---------- SLEEP  ----------
def get_sleep_log_str(sleep_log):
    sleep_log_str = ''
    for sleep in sleep_log:
        time1 = datetime.strptime(sleep[0], '%H:%M:%S')
        if sleep[1] == "0":
            status = "Заспа"
            sleep_edit = f"           {status} во {sleep[0]}  -  {sleep[2]}\n"
        else:
            status = "Се разбуди"
            time2 = datetime.strptime(sleep[1], '%H:%M:%S')
            slept = time2 - time1
            sleep_edit = (f"{status} во {sleep[1]}  -  {sleep[2]}, "
                          f"     спиела: {slept}\n")
        sleep_log_str += sleep_edit
    return sleep_log_str


"""def get_total_sleep(sleep_log):
    print("Hello get_total_sleep", sleep_log)


def get_sleep_str(total_sleep_dic):
    print("Hello from get_sleep_str", total_sleep_dic)"""