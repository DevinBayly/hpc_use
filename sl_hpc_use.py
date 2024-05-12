import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import random
import streamlit.elements.image as st_image
import requests as rq
from PIL import Image
# get the custom component
from streamlit_component_x.src.streamlit_component_x import example
# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`


labels= ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents= ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]


#concept_names, concept_counts, concept_parents = json.load(open('found_concepts.json', "r"))
#
## Sort by 
#for _ in range(3):
#    for i, concept_name in enumerate(concept_parents):
#        if concept_name != "" and concept_name not in concept_names:
#            concept_names.pop(i)
#            concept_counts.pop(i)
#            concept_parents.pop(i)
#            # print(concept_name)
#            # print("Removed " + concept_name)
#
#    print("Leftovers")
#    for i, concept_name in enumerate(concept_parents):
#        if concept_name != "" and concept_name not in concept_names:
#            # print(concept_name)
#            pass
#
#
#"""
## Publications by Users of University of Arizona HPC
#
#This app presents an interactive data visualization allowing a user to explore the scientific fields that our HPC users published to in the time range 2016-2022. 
#
#Interaction instructions:
#* Clicking on an individual square will expand the view and present the sub-fields for the selected square, this allows you to "go down" the tree
#* To "go back up" the tree, click on the ribbon at the top 
#* Now please click fullscreen to explore further
#You are encouraged to full screen the tree map below. 
#"""
##fig.update_traces(marker_cornerradius=5)
## st.plotly_chart(fig)
#
#print("running example from test_custom")
res = example([list(labels),list(parents)],key="fixed")
# making a sidebar
# "with" notation
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a list of Cluster User Names")
    if uploaded_file is not None:
        text = open(uploaded_file).read_lines()
        st.write(text)

    name = st.text_input("Enter the Institution Name", "University of Arizona")
    res = rq.get(f"https://api.ror.org/organizations?query={name}").json()
    if res:
        items = res.get("items")
        if items:
            best_res = items[0]
            st.write(best_res["id"])

    
    #specifying the range in time that we want to inspect
    start_date, end_date = st.select_slider(
        "Select a range of years to survey user publications",
        options=list(range(2016,2023)),
        value=(2016, 2017))
    st.write("You selected years between", start_date, "and", end_date)
#if res and 'finished' not in res:
#    st.markdown(res)
#    df = pd.read_csv("works.csv")
#    print(df.shape,res)
#    inds = df.concepts.str.contains(str(res),na=False)
#    # print(inds)
#    sub = df[inds].head(n=20)
#    print(sub)
#    st.table(sub)
