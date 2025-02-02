import streamlit as st
import em_functions

# momentalna vozrast na Emilija
# notiikacii za hranenje i spienje

###  APLIKACIJA   ###

# inputi od GUI:
def ispieno():
    try:
        ispi = int(st.session_state["ml_input"])
        vreme = str(st.session_state["ml_time"])
        date = st.session_state["date_input"]
        date = str(date)
        milk_type=''
        if st.session_state["ml_majka"]:
            milk_type="Mama's"
        elif st.session_state["ml_formula"]:
            milk_type="Formula"
        input_log = [] #f"[{vreme}, {ispi}, {milk_type}, {date}]\n"
        input_log.extend([vreme, ispi, milk_type, date])
        em_functions.write_ml_log(input_log, filepath='ml_log.txt')
    except UnicodeEncodeError:
        st.toast("Само нумеричка вредност може да се внесе!")
    except ValueError:
        st.toast("Само нумеричка вредност може да се внесе!")




# Web App GUI
st.title("Лејди Емилија")  # naslovot go printa prv, podnaslov vtor i tn.

# ---------- FEED ----------
# vnesi gi site obroci od ml_log.txt so CSV
ml_log = em_functions.get_ml_log()
ml_log.sort(reverse=True)

st.subheader("Дневник за исхрана.")
#datum i vreme za ml
st.date_input("Датум:", key="date_input", format="DD.MM.YYYY")
st.time_input("Време:", key="ml_time", step=300)
st.text_input(label="Колку млеко има испиено?", placeholder="внеси ml",
              key="ml_input")
st.button("Мајчино", key="ml_majka", on_click=ispieno)
st.button("Формула", key="ml_formula", on_click=ispieno)
# log vo denot koga e posledno pieno
ml_log_str = em_functions.get_ml_log_str(ml_log)
st.text_area( "Лог за храна:", value=ml_log_str, height=136)

# ----- SLEEP ----------
# vnesi gi site obroci od ml_log.txt so CSV
sleep_log = em_functions.get_sleep_log()
sleep_log.sort(reverse=True)

#sleep_check = {"if sleep then must wake, if wake must sleep"}
# log za posledno spienje vo denot so total vreme
#sleep_log = {"sleep-date":"22:30", "wake-date":"04:10"}
# log za spieni saati dnevno
st.subheader("Дневник за спиење.")
st.date_input("Датум:", key="date_sleep", format="DD.MM.YYYY")
st.time_input("Време", key="sleep_time", step=300)
st.button("Заспа", key="sleep_ok")
st.button("Разбуди", key="wakeup_ok")
sleep_log_str = em_functions.get_sleep_log_str(sleep_log)
st.text_area( "Лог за сон:", value=sleep_log_str, height=136)

# --------- Total na den --------
st.subheader("Вкупно храна и сон во ден.")
#spremanje i podreduvanje dnevni ml
ml_log_dic = em_functions.get_total_ml(ml_log)

# dnevnite ml od desc vo string za printanje:
total_daily = em_functions.get_ml_str(ml_log_dic)
st.text_area( "Вкупно испиени ml на ден:", value=total_daily, height=136)

st.session_state  # dopolnitelen prozor koj ni dava realtime input
# sekoj item mora da ima key za da bide prikazan vo state
