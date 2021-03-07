function solve() {
    const busInfo = document.querySelector('.info');
    const departButton = document.getElementById('depart');
    const arriveButton = document.getElementById('arrive');
    let nextBusStop = 'depot';

    function depart() {
        const url = `http://localhost:3030/jsonstore/bus/schedule/${nextBusStop}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                busInfo.textContent = `Next stop ${nextBusStop[0].toUpperCase() + nextBusStop.slice(1)}`;
                departButton.disabled = 'true';
                arriveButton.removeAttribute('disabled');
                nextBusStop = data.next;
            })
    }

    function arrive() {
        let busStopName = busInfo.textContent.split(' ').slice(-1).join('');
        busInfo.textContent = `Arriving at ${busStopName}`;
        departButton.removeAttribute('disabled');
        arriveButton.disabled = 'true';
    }

    return {
        depart,
        arrive
    };
}

let result = solve();