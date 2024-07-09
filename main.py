import streamlit as st
import os


class Mittel:
    colors = {
        "Feuerwehr" : "red",
        "Polizei" : "blue",
        "Sanitaet" : "green",
        "Zivilschutz" : "orange",
        "Andere" : "black"
    }

    def __init__(self, org, mit, free=True, last=[]):
        self.org = org
        self.mit = mit
        self.free = free
        self.last = last
        self.tk = st.session_state["toggle_key"]
        st.session_state["toggle_key"] += 1

    def draw(self):
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            if not self.org in self.colors:
                c = "black"
            else:
                c = self.colors[self.org]

            with col1:
                st.markdown(f":{c}[{self.org}]")

            with col2:
                st.markdown(self.mit)

            with col3:
                self.free = st.toggle("Im Einsatz", key=self.tk)



with st.sidebar:
    workingdir = st.text_input("Pfad zum Ordner", "C:\\Users\\User\\Desktop")
    if not os.path.exists(workingdir):
        st.error("Pfad nicht gefunden")

    filename = st.text_input("Dateiname", "Mitteluebersicht")
    if filename[-4:] != ".txt":
        filename = filename + ".txt"


    filepath = os.path.join(workingdir, filename)



if "mittel_list" not in st.session_state:
    st.session_state["mittel_list"] = []
if "toggle_key" not in st.session_state:
    st.session_state["toggle_key"] = 0

with st.container(border=True):
    organisation = st.selectbox(
                "Organisation",
                (
                    "Feuerwehr",
                    "Polizei",
                    "Sanitaet",
                    "Zivilschutz",
                    "Andere"
                ),
                index=None,
            )

    mittel = st.text_input("Mittel")

    if st.button("Hinzufuegen"):
        if organisation == None or mittel == None:
            st.error("Organisation und Mittel muessen ausgefuellt werden.")
        else:
            st.session_state["mittel_list"].append(Mittel(org=organisation, mit=mittel))


st.session_state["mittel_list"].sort(key=lambda x: x.org + x.mit)
for m in st.session_state["mittel_list"]:
    m.draw()

        
