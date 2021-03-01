async function processRequest(id) {
    let request = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${id}`);
    return await request.json();
}

async function showStops(json) {
    document.querySelector('#stopName').textContent = json.name;
    let busUl = document.querySelector('#buses');
    Object.keys(json.buses)
        .forEach(bus => {
            busUl.innerHTML += `<li>Bus ${bus} arrives in ${json.buses[bus]} minutes</li>`;
        })
}


async function getInfo() {
    let busStop = document.querySelector('#stopId').value;

    try {
        Array.from(document.querySelector('#buses').children)
            .forEach(e => e.remove());
        let json = await processRequest(busStop);
        await showStops(json);
    } catch (err) {
        document.querySelector('#stopName').textContent = 'Error';
    }
}