from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_component_x,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
print("frontend dir is ",frontend_dir)
_component_func = components.declare_component(
	"streamlit_component_x", path=str(frontend_dir)
)
# basic structure for treemap

labels= ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents= ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]


# Create the python function that will be called
def streamlit_component_x(data,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        data=data,
        key=key,
    )

    return component_value


def main(data):
    st.write("## Example main")
    value = streamlit_component_x(data)

    st.write(value)
    print(value)

def example(data,key=None):
    # print("inside of example",data)
    st.write("### Interactive Topic Treemap")
    value = streamlit_component_x(data = data,key=key)
    print("value is",value)
    return value

if __name__ == "__main__":
    main([labels,parents])
