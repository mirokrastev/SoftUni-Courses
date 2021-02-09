function solve(request) {
    let validMethods = ['GET', 'POST', 'DELETE', 'CONNECT'];
    let validVersions = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];
    let regexPattern = /<|>|\\|&|'|"/g;

    if (!validMethods.includes(request.method)) {
        throw new Error('Invalid request header: Invalid Method');
    }
    if (!request.uri || !request.uri.includes('.')) {
        throw new Error('Invalid request header: Invalid URI');
    }
    if (!validVersions.includes(request.version)) {
        throw new Error('Invalid request header: Invalid Version');
    }
    if (!request.hasOwnProperty('message') || request.message.match(regexPattern)) {
        throw new Error('Invalid request header: Invalid Message');
    }
    return request
}
