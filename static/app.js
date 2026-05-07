// Firstly, cosmetics.
const hostnameElement = document.getElementById("hostname")
const title = document.getElementById("title");
const cout = document.getElementById("commandoutput"); // The programmers yearn for cout

title.innerText = `G.O.H. @ ${window.location.host}`

hostnameElement.innerText = window.location.host
cout.innerText = ""
cout.innerText += "[Info] Command output will appear here."

// Now.. stuff.
const colourPicker = document.getElementById("colourPicker");
const powerState = document.getElementById("powerState");
const brightnessSlider = document.getElementById("brightnessSlider");

function printcout(text) {
    cout.innerText = `[RESPONSE] ${text}\n` + cout.innerText // cursed.
}

function hexToRgb(hex) {
    hex = hex.replace(/^#/, "");
    let bigint = parseInt(hex, 16);
    let r = (bigint >> 16) & 255;
    let g = (bigint >> 8) & 255;
    let b = bigint & 255;
    return { r, g, b };
}

let colourTimeout;

colourPicker.addEventListener("input", () => {
    clearTimeout(colourTimeout);

    colourTimeout = setTimeout(() => {
        const rgb = hexToRgb(colourPicker.value);


        fetch(`/goh/api/set_colour?rgb=${rgb.r}-${rgb.g}-${rgb.b}`)
            .then(res => res.json())
            .then(data => {
                printcout(data.message);
            })
            .catch(err => console.error("Fetch error:", err));
    }, 200);
});

powerState.addEventListener("input", () => {
    const state = powerState.checked;

    const req = fetch(`/goh/api/set_power?state=${String(state)}`)
        .then(res => res.json())
        .then(data => {
            printcout(data.message);
        });

})

let brightnessTimeout;
brightnessSlider.addEventListener("input", () => {
    clearTimeout(brightnessTimeout);
    brightnessTimeout = setTimeout(() => {
        fetch(`/goh/api/set_brightness?percent=${brightnessSlider.value}`)
            .then(res => res.json())
            .then(data => {
                printcout(data.message);
            });
    }, 200);
});
