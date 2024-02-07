# instructions
use https://blog.streamlit.io/how-to-build-your-own-streamlit-component/
and https://d3js.org/getting-started#d3-in-vanilla-html to test out 

Also something about the codespace gets the streamlit install wrong, so use a .venv with this 
```
python -m venv .venv
source .venv/bin/activate
pip install streamlit
```
# streamlit-component-x

Streamlit component that allows you to do X

## Installation instructions 

```sh
pip install streamlit-component-x
```

## Usage instructions

```python
import streamlit as st

from streamlit_component_x import streamlit_component_x

value = streamlit_component_x()

st.write(value)
