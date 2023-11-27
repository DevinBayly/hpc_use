import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objects as go
import json

concept_names, concept_counts, concept_parents = json.load(open('found_concepts.json', "r"))

# Sort by 
for _ in range(3):
    for i, concept_name in enumerate(concept_parents):
        if concept_name != "" and concept_name not in concept_names:
            concept_names.pop(i)
            concept_counts.pop(i)
            concept_parents.pop(i)
            print(concept_name)
            print("Removed " + concept_name)

    print("Leftovers")
    for i, concept_name in enumerate(concept_parents):
        if concept_name != "" and concept_name not in concept_names:
            print(concept_name)

fig = go.Figure(go.Treemap(
    labels = list(concept_names),
    parents = list(concept_parents),
    values = list(concept_counts),
    textinfo = 'label+value',
    maxdepth = 2
))
#fig.update_traces(marker_cornerradius=5)
st.plotly_chart(fig)