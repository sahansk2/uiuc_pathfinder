
function getEmptyParams(knownParams) {
    let emptySearchParams = {}
    for (let p of knownParams) {
        emptySearchParams[p.name] = "";
        if (p.nullable) {
            emptySearchParams[getNullName(p.name)] = false;
        }
    }
    return emptySearchParams
}

function getNullName(param) {
    return `${param}Null`
}

export {
    getNullName,
    getEmptyParams
}