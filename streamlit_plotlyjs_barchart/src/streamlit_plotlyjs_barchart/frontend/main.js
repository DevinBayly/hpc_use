//import { Streamlit, RenderData } from "streamlit-component-lib"
// Add text and a button to the DOM. (You could also add these directly
// to index.html.)
// Add a click handler to our button. It will send data back to Streamlit.
let numClicks = 0
let completed = false
let isFocused = false
/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event){
  // Get the RenderData from the event
  if (completed) return
  const data = event.detail
  // weird nesting
  // assume that first element is xs, ys come next
  let barData = data.args.data

  // Maintain compatibility with older versions of Streamlit that don't send
  // a theme object.
  if (data.theme) {
    // Use CSS vars to style our button border. Alternatively, the theme style
    // is defined in the data.theme object.
    const borderStyling = `1px solid var(${isFocused ? "--primary-color" : "gray"
      })`
  }

  // Disable our button if necessary.

  // RenderData.args is the JSON dictionary of arguments sent from the
  // Python script.
  let name = data.args["name"]
  console.log("passed ", name)

  // Show "Hello, name!" with a non-breaking space afterwards.
  let gd = document.querySelector("#gd")
  // for some reason the width and height part here mess up the drawing
  let t = [{ type: "bar", x:barData[0],y:barData[1]}]

var layout = {

  autosize:true,
  showlegend: false,
  automargin:true,
  xaxis:{
    type:"category"
  }
};


  Plotly.newPlot("gd", t,layout,{staticPlot:true})
  gd.on("plotly_click", (e => {
    console.log(e)
    // let t = e.points[0].label
    // console.log("dispatched", t)
    // Streamlit.setComponentValue(t)
  }))
  // this is to control stuff like the resizing button
  let btn = document.querySelector("button")
  if (btn) {

  btn.onclick = () => {
    let update = {
      width:1920,
      height:1080
    }
    Plotly.relayout("gd", update);
    let bb = gd.getBoundingClientRect()
    console.log(bb)
    // We tell Streamlit to update our frameHeight after each render event, in
    // case it has changed. (This isn't strictly necessary for the example
    // because our height stays fixed, but this is a low-cost function, so
    // there's no harm in doing it redundantly.)
    // set height to only this much plus a buffer
    Streamlit.setFrameHeight(bb.height)
  }
  }

  let bb = gd.getBoundingClientRect()
  console.log(bb)
  // We tell Streamlit to update our frameHeight after each render event, in
  // case it has changed. (This isn't strictly necessary for the example
  // because our height stays fixed, but this is a low-cost function, so
  // there's no harm in doing it redundantly.)
  // set height to only this much plus a buffer
  Streamlit.setFrameHeight(bb.height)
  completed=true
}

// Attach our `onRender` handler to Streamlit's render event.
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
