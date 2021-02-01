function result(func) {
    return func.bind(null, ',', '$', true)
}