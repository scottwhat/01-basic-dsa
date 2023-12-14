const graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

const depthFirstPrint = (graph, source) => {
    console.log(source)
    for (let neighbor of graph[source]) {
        depthFirstPrint(graph, neighbor)
    }
}

depthFirstPrint(graph, 'f')