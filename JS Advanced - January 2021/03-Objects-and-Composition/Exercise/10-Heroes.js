function solve() {
    return {
        mage(name) {
            return {name, health: 100, mana: 100, cast(spellName) { this.mana--; return `${this.name} cast ${spellName}`}}
        },
        fighter(name) {
            return {name, health: 100, stamina: 100, fight() { this.stamina--; return `${this.name} slashes at the foe!` }}
        }
    }
}