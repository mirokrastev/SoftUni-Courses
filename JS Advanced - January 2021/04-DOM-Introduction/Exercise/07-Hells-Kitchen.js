function solve() {
	document.getElementById('btnSend').addEventListener('click', getInput)

    function getInput() {
        let textarea = document.querySelector('#inputs textarea');
        let parsedInput = JSON.parse(textarea.value)
        let output = [];

        for (let restaurant of parsedInput) {
            let [restaurantName, staff] = restaurant.split(' - ');
            staff = staff.split(', ').map(person => {
            let [personName, salary] = person.split(' ');
            return {personName, 'salary': Number(salary)};
            })
            let sameRestaurant = output.find(el => el.restaurantName === restaurantName);
            if (!(sameRestaurant === undefined)) {
                sameRestaurant.staff = [...sameRestaurant.staff, ...staff];
                output.splice(output.indexOf(sameRestaurant), 1);
            }
            else {
                sameRestaurant = {restaurantName, staff};
            }
            sameRestaurant.staff.sort((personOne, personTwo) => personTwo.salary - personOne.salary);
            sameRestaurant.avgSalary = sameRestaurant.staff.reduce((a, c) => a + c.salary, 0) / sameRestaurant.staff.length;
            output.push(sameRestaurant);
        }
        output.sort((restaurantOne, restaurantTwo) => restaurantTwo.avgSalary - restaurantOne.avgSalary || 0);
        let bestRestaurant = output[0];

        let bestRestaurantPTag = document.querySelector('#bestRestaurant p');
        let workersPTag = document.querySelector('#workers p');

        let [name, salary, bestSalary] = [bestRestaurant.restaurantName, bestRestaurant.avgSalary, bestRestaurant.staff[0]]
        bestRestaurantPTag.textContent = `Name: ${name} Average Salary: ${salary.toFixed(2)} Best Salary: ${bestSalary.salary.toFixed(2)}`
        let bestWorkers = bestRestaurant.staff.map(obj => `Name: ${obj.personName} With Salary: ${obj.salary}`);
        workersPTag.textContent = bestWorkers.join(' ');
	}
}