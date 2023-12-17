const graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

const depthFirstPrint = (graph, source) => {
    //strart with source
    const stack = [source]

    //steps 
    // 1. start at source node, push to stack
    // 2. current = stack.pop 
    // 3. process / do what ever you want on current
    // 4. add all neighbours from currents array of edges,
    // 5. while loop continues 


    // while (stack.length > 0) {
    //     const current = stack.pop();
    //     console.log(current)

    //     for (let neighbor of graph[current]) {
    //         stack.push(neighbor)
    //     }
    // }

    while (stack.length > 0) {
        let current = stack.pop();
        console.log(current)

        for (let child of graph[current]) {
            stack.push(child)
        }
    }
}



depthFirstPrint(graph, 'f')




