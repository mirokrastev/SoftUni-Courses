function attachEventsListeners() {
    let daysText = document.getElementById('days');
    let hoursText = document.getElementById('hours');
    let minutesText = document.getElementById('minutes');
    let secondsText = document.getElementById('seconds');

    let daysBtn = document.getElementById('daysBtn');
    let hoursBtn = document.getElementById('hoursBtn');
    let minutesBtn = document.getElementById('minutesBtn');
    let secondsBtn = document.getElementById('secondsBtn');

    daysBtn.addEventListener('click', convertFromDays);
    hoursBtn.addEventListener('click', convertFromHours);
    minutesBtn.addEventListener('click', convertFromMinute);
    secondsBtn.addEventListener('click', convertFromSeconds);

    function convertFromDays() {
        let daysValue = Number(daysText.value);

        hoursText.value = daysValue * 24;
        minutesText.value = daysValue * 1440;
        secondsText.value = daysValue * 86400;
    }

    function convertFromHours() {
        let hoursValue = Number(hoursText.value);

        daysText.value = hoursValue / 24;
        minutesText.value = hoursValue * 60;
        secondsText.value = hoursValue * 3600;
    }

    function convertFromMinute() {
        let minutesValue = Number(minutesText.value);

        daysText.value = minutesValue / 1400;
        hoursText.value = minutesValue / 60;
        secondsText.value = minutesValue * 60;
    }

    function convertFromSeconds() {
        let secondsValue = Number(secondsText.value);

        daysText.value = secondsValue / 86400;
        hoursText.value = secondsValue / 3600;
        minutesText.value = secondsValue / 60;
    }
}