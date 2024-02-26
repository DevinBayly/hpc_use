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
  let treemapData = data.args.data
  console.log("data is",data)

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
  let t = [{ type: "treemap", labels: treemapData
  [0], parents: treemapData[1] }]
  Plotly.newPlot("gd", t)
  let l = document.querySelector("#selected") 
  gd.on("plotly_click", (e => {
    console.log(e)
    let t = e.points[0].label
    l.innerHTML = t
    console.log("dispatched", t)
  }))


  // We tell Streamlit to update our frameHeight after each render event, in
  // case it has changed. (This isn't strictly necessary for the example
  // because our height stays fixed, but this is a low-cost function, so
  // there's no harm in doing it redundantly.)
  Streamlit.setFrameHeight()
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

// // The `Streamlit` object exists because our html file includes
// // `streamlit-component-lib.js`.
// // If you get an error about "Streamlit" not being defined, that
// // means you're missing that file.

// function sendValue(value) {
//   Streamlit.setComponentValue(value)
// }

// /**
//  * The component's render function. This will be called immediately after
//  * the component is initially loaded, and then again every time the
//  * component gets new data from Python.
//  */
// function onRender(event) {
//   // Only run the render code the first time the component is loaded.
//   console.log("rendering")
//   if (!window.rendered) {
//     // You most likely want to get the data passed in like this
//     // const {input1, input2, input3} = event.detail.args
//     sendValue(["finished","code"])
//     // You'll most likely want to pass some data back to Python like this
//     // sendValue({output1: "foo", output2: "bar"})
//     window.rendered = true
//   }
// }

// // Render the component whenever python send a "render event"
// Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// // Tell Streamlit that the component is ready to receive events
// Streamlit.setComponentReady()
// // Render with the correct height, if this is a fixed-height component
// Streamlit.setFrameHeight(800)
