const fs = require('fs');
const fromGoogle = require('./pigeons.json')
const pigeons = fromGoogle.items.map(item => {
    return item.link;
})

html = makeHtml(pigeons)

fs.writeFile("index.html", html, (err, file) => {
    if (err) {
        throw err
    }
    console.log("File written")
})

function makeHtml(pigeons) {
    let html = "<!doctype html><title>Pigeon Pictures</title><meta charset=\"utf-8\">"
    html += `<style>
        body {
            background: url(${pigeons[0]});
            background-size: cover;
            text-align: center
        }
        img {
            max-width: 100vw
        }
    </style>`
    for (let link of pigeons) {
        html += `<img alt="pigeon" src="${link}">`
    }
    return html
}
