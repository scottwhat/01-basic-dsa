class Node {
    constructor(val) {
        this.val = val
        this.left = null
        this.right = null
    }

}

const a = new Node(-1);
const b = new Node(-6);
const c = new Node(-5);
const d = new Node(-3);
const e = new Node(-4);
const f = new Node(-13);
const g = new Node(-2);
const h = new Node(-2);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     /       \
//    -2       -2


const treeMinValue = (root) => {
    //min questions use infinity,
    //max questions use negative infinity 
    if (root === null) return Infinity

    leftMin = treeMinValue(root.left)
    rightMin = treeMinValue(root.right)

    //recurse back up the tree returning the minimum vals 
    return Math.min(root.val, leftMin, rightMin)
}

//Expect -13
console.log(treeMinValue(a))