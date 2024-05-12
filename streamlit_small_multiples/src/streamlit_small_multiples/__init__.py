from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_small_multiples,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
print("frontend dir is ",frontend_dir)
_component_func = components.declare_component(
	"streamlit_small_multiples", path=str(frontend_dir)
)
# basic structure for treemap



# Create the python function that will be called
def streamlit_small_multiples(data,
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
    value = streamlit_small_multiples(data)

    st.write(value)
    print(value)

def example(data,key=None):
    print("inside of example",data)
    st.write("#### Topics Small Multiples ")
    value = streamlit_small_multiples(data = data,key=key)
    print("value is",value)
    return value

if __name__ == "__main__":
    main([labels,parents])
