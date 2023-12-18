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

    //for loopn gives an implicit return because if theres nothing 
    //to iterate it breaks without making the recursive call
    for (let neighbor of graph[source]) {
        //recursive reduction, pass the child as the new source
        depthFirstPrint(graph, neighbor)
    }
}

depthFirstPrint(graph, 'f')