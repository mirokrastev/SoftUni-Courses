import {setupUserNav} from "./navbar.js";
import {setupHome} from "./home.js";

export async function main() {
    setupUserNav();
    setupHome();
}

main();