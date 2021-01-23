function solve(obj) {
    if (!obj.dizziness) return obj;
    obj.dizziness = false;
    obj.levelOfHydrated += (obj.weight * obj.experience) / 10;
    return obj;
}