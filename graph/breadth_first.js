//must use queue
//backwards queue commands

//array.shift removes first element
//array.push adds to end 
const breadthFirstPrint = (graph, source) => {
    const queue = [source]
    while (queue.length > 0) {
        current = queue.shift()
        console.log(current)
        for (let neighbor of graph[current]) {
            queue.push(neighbor)
        }
    }
}

const graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

breadthFirstPrint(graph, 'f')