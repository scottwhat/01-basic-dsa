
const hasPath = (graph, src, dst) => {

    const queue = [src]

    while (queue.length > 0) {

        //current = take the first out of the array, unshift
        //for loop (current neighbors add to queue .append)
        //

        let current = queue.shift()
        if (current === dst) return true;

        for (let neighbor of graph[current]) {
            queue.push(neighbor)
        }
    }
    return false
}

const graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

console.log(hasPath(graph, 'f', 'k'))