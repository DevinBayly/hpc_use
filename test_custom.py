import streamlit as st
import random
import streamlit.elements.image as st_image
from PIL import Image
# get the custom component
from streamlit_component_x.src.streamlit_component_x import example
# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

import pandas as pd
import numpy as np

labels= ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents= ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]

# pass the labels and parents

# Create an instance of our component with a constant `name` arg, and
# print its output value.
print("running example from test_custom")
example([labels,parents])
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
