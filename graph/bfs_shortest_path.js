

//BFS shortest path


const shortestPath = (edges, nodeA, nodeB) => {
    const graph = buildGraph(edges);
    const visited = new Set();
    visited.add(nodeA)
    const queue = [];
    const distance = 0
    queue.push([nodeA, distance])



    while (queue.length > 0) {
        //pop the first node off the queue
        const [node, distance] = queue.shift()
        if (node === nodeB) return distance;

        for (let neighbor of graph[node]) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor)
                queue.push([neighbor, distance + 1])
            }
        }
    }
    return -1;
};

const buildGraph = (edges) => {
    const graph = {};

    for (let edge of edges) {
        const [a, b] = edge;
        if (!(a in graph)) graph[a] = [];
        if (!(b in graph)) graph[b] = [];

        graph[a].push(b);
        graph[b].push(a);
    }

    return graph;
};


const edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
];

//2 
console.log(shortestPath(edges, 'w', 'z')) 