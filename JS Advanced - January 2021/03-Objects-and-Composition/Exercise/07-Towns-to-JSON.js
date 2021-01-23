function solve(args) {
    let towns = [];

    for (let i = 1; i < args.length; i++) {
        let [town, latitude, longitude] = args[i]
            .split('|')
            .filter(e => e !== '')
            .map(e => e.trim());

        towns.push({
            Town: town,
            Latitude: Number(Number(latitude).toFixed(2)),
            Longitude: Number(Number(longitude).toFixed(2))
        });
    }

    console.log(JSON.stringify(towns));
}