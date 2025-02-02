import streamlit as st
import em_functions


def ispieno():
    ispi = st.session_state["ml_input"] #+ "\n"
    vreme = str(st.session_state["ml_time"])
    date = st.session_state["date_input"]
    date = str(date)
    milk_type=''
    if st.session_state["ml_majka"]:
        milk_type="Mamas"
    elif st.session_state["ml_formula"]:
        milk_type="Formula"
    input_log = [] #f"[{vreme}, {ispi}, {milk_type}, {date}]\n"
    input_log.extend([vreme, ispi, milk_type, date])
    print(input_log)
    #ml_log.append(input_log)
    #print(ml_log)
    #ml_log.sort(reverse=True)
    em_functions.write_ml_log(input_log, filepath='ml_log.txt')



# vnesi gi site hranenja
ml_log = em_functions.get_ml_log()
print("prvo chitanje na ml_log:", ml_log)

# log vo denot koga e posledno pieno
#key_date = "datumot"
# log za sekoj den kolku e vkupno ispieno
#ml_daily = {}
# proverka dali spie ili e budna
#sleep_check = {"if sleep then must wake, if wake must sleep"}

# log za posledno spienje vo denot so total vreme
#sleep_log = {"sleep-date":"22:30", "wake-date":"04:10"}
# log za spieni saati dnevno

# Web App GUI
st.title("Лејди Емилија")  # naslovot go printa prv, podnaslov vtor i tn.
st.subheader("Апликација за следење на јадење и спиење.")

st.date_input("Datum", key="date_input", format="DD.MM.YYYY")
st.time_input("Последно е јадена во:", key="ml_time", step=300)
st.text_input(label="Колку млеко има испиено?", placeholder="внеси ml",
              key="ml_input")
st.button("Мајчино", key="ml_majka", on_click=ispieno)
st.button("Формула", key="ml_formula", on_click=ispieno)
ml_log_str = ""
for meal in ml_log:
    #meal = list(meal)
    #st.write(meal)
    meal_edit = f"{meal[0]} - {meal[1]} ml - {meal[2]} - {meal[3]}"
    ml_log_str = ml_log_str + meal_edit
st.text_area( "Лог за храна:", value=ml_log_str, height=68)
st.time_input("Заспа во:", key="sleep_time", step=300)
st.button("Ok", key="sleep_ok")
st.time_input("Се разбуди во:", key="wakeup_time", step=300)
st.button("Ok", key="wakeup_ok")
#st.code(em_functions.get_sleep_log())
st.session_state  # dopolnitelen prozor koj ni dava realtime input
# sekoj item mora da ima key za da bide prikazan vo state
