import { getGraph } from './user/util'

const graphFetch = (url, data) => {
    console.log("Fetching from URL", url, "at", new Date())
    return (new Promise(resolve => resolve({...getGraph(data)})))
}

const fakeFetch = (url, data) => {
    console.log("Fetching from URL", url, "at", new Date())
    return (new Promise(resolve => resolve(data)))
}

const failFetch = (url, data) => {
    console.log("Failing URL fetch", url, "at", new Date())
    return (new Promise((_, reject) => reject(data)))
}

export {
    graphFetch,
    fakeFetch,
    failFetch
}
