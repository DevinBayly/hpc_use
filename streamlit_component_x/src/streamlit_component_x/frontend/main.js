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
  let customevent = new CustomEvent("start", { "detail": name })
  if (gd) {
    console.log("adding listener")
    gd.addEventListener("send", () => {

      let sel = document.querySelector("#selected")
      if (sel) Streamlit.setComponentValue(sel.innerHTML)
    })
    console.log("dispatching from javascript")
    gd.dispatchEvent(customevent)
    gd.addEventListener("start",
      (
        function (e) {
          console.log("this ran ", e)
          let t = [{ type: "treemap", labels: e.detail[0], parents: e.detail[1] }]
          Plotly.newPlot("gd", t)
          let l = document.querySelector("#selected"), n = document.querySelector("#gd")
          n.on("plotly_click", (e => {
            console.log(e)
            let t = e.points[0].label
            l.innerHTML = t
            let o = new CustomEvent("send", { detail: t })
            n.dispatchEvent(o)
            console.log("dispatched", o)
          }))
        }
      )
    )
  }


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
