import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import random
import streamlit.elements.image as st_image
from PIL import Image
# get the custom component
from streamlit_component_x.src.streamlit_component_x import example
# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`


labels= ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents= ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]


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

print("running example from test_custom")
res = example([list(concept_names),list(concept_parents)],key="fixed")

st.markdown(res)
df = pd.read_csv("works.csv")
inds = df.concepts.str.contains(str(res),na=False)
# print(inds)
sub = df[inds].head(n=20)
st.table(sub)
# pass the labels and parents

# Create an instance of our component with a constant `name` arg, and
# print its output value.
# selected = my_component([labels,parents],key="fixed")
# st.markdown(selected)

# st.markdown("---")
# st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
# name_input = st.text_input("Enter a name", value="Streamlit")
# num_clicks = my_component(name_input,key="foo")
# st.markdown("You've clicked %s times!" % int(num_clicks))
