function solve(area, vol, input) {
    return JSON.parse(input).map(object => ({area: area.call(object), volume: vol.call(object)}));
}