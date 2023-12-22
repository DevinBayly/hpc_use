import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objects as go
import json
import sys
sys.path.append("./my_component")
from my_component import my_component

concept_names, concept_counts, concept_parents = json.load(open('found_concepts.json', "r"))

# Sort by 
for _ in range(3):
    for i, concept_name in enumerate(concept_parents):
        if concept_name != "" and concept_name not in concept_names:
            concept_names.pop(i)
            concept_counts.pop(i)
            concept_parents.pop(i)
            # print(concept_name)
            # print("Removed " + concept_name)

    print("Leftovers")
    for i, concept_name in enumerate(concept_parents):
        if concept_name != "" and concept_name not in concept_names:
            # print(concept_name)
            pass

# fig = go.Figure(go.Treemap(
#     labels = list(concept_names),
#     parents = list(concept_parents),
#     values = list(concept_counts),
#     textinfo = 'label+value',
#     maxdepth = 2
# ))
# skip this and instead use the custom one built to make callbacks work

"""
# Publications by Users of University of Arizona HPC

This app presents an interactive data visualization allowing a user to explore the scientific fields that our HPC users published to in the time range 2016-2022. 

Interaction instructions:
* Clicking on an individual square will expand the view and present the sub-fields for the selected square, this allows you to "go down" the tree
* To "go back up" the tree, click on the ribbon at the top 
* Now please click fullscreen to explore further
You are encouraged to full screen the tree map below. 
"""
#fig.update_traces(marker_cornerradius=5)
# st.plotly_chart(fig)

res = my_component([list(concept_names),list(concept_parents)],key="fixed")

st.markdown(res)
df = pd.read_csv("works.csv")
inds = df.concepts.str.contains(str(res),na=False)
# print(inds)
sub = df[inds].head(n=20)
st.table(sub)