# Continuous Learning Assessment – 2
## Algorithm Battle: Which Data Structure Wins?

**Institution:** SRM Institute of Science and Technology, Tiruchirappalli  
**Application:** Student Record Search System  
**Student Name:** ____________________  
**Register Number:** ____________________  
**Course / Section:** ____________________

## Part A — Problem Selection

### Problem
The Student Record Search System stores student details such as register number, name, department, and year. A user searches for a student using the unique register number.

### Why efficient searching is required
A college may maintain hundreds or thousands of student records. Searching sequentially through every record can take O(n) time. A suitable data structure can reduce the number of comparisons and make record retrieval faster.

### Why compare BST, AVL, and hashing?
BST and AVL maintain keys in sorted order and support ordered traversal. A normal BST can become skewed, while AVL rotations maintain height balance. Hashing maps a key to a table index and can provide very fast average-case lookup. Linear probing resolves collisions by checking subsequent slots.

## Part B — Implementation
The project implements insertion and searching in all three structures. BST and AVL also provide inorder traversal. The hash table uses linear probing for collision resolution. Refer to the Python source files for implementation details.

## Part C — Mini Experiment

- Dataset: 40 fictional records from `dataset.py`.
- Insertion order: identical for BST, AVL, and hashing.
- Successful search: five register numbers that exist in the dataset.
- Unsuccessful search: five register numbers that do not exist in the dataset.
- Insertion: all 40 records are inserted into each structure; the interactive menu also permits a new record to be inserted into all three.

Run `python experiment.py` and paste the actual console output / `results.csv` observations below.

### Experimental observations
| Parameter | BST | AVL | Hashing |
|---|---|---|---|
| Successful search comparisons (average) | Fill from output | Fill from output | Fill from output |
| Unsuccessful search comparisons (average) | Fill from output | Fill from output | Fill from output |
| Insertion observation | Fill from output / code | Fill from output / code | Fill from output |
| Height (levels) | Fill from output | Fill from output | Not applicable |
| Collisions during insertion | Not applicable | Not applicable | Fill from output |

## Part D — Algorithm Battle

Discuss the measured results:
1. Compare average successful-search comparisons.
2. Compare average unsuccessful-search comparisons.
3. Explain how the insertion order affects the ordinary BST.
4. Explain how AVL rotations control tree height.
5. Explain how linear probing handles collisions and how clustering can affect performance.

## Part E — Final Verdict

**Recommended structure:** ____________________

Justification must refer to the actual measured output. For a workload dominated by exact register-number lookups, hashing is often the strongest choice when the load factor is controlled. AVL is a strong choice when predictable logarithmic search and sorted traversal are both important. A plain BST is simple but can become unbalanced depending on insertion order. State which one wins for this experiment using your own output, rather than assuming a winner in advance.

## Conclusion
The experiment demonstrates that data-structure performance depends on the operations required, input order, balancing, hash function, and collision pattern. The same dataset and test keys were used to make the comparison fair.

## Viva preparation
1. **What is a BST?** A binary tree in which keys smaller than a node are placed in its left subtree and larger keys in its right subtree.
2. **What is an AVL tree?** A self-balancing BST in which the balance factor of every node is -1, 0, or +1.
3. **What is a balance factor?** Height(left subtree) minus height(right subtree).
4. **Name the AVL rotations.** LL, RR, LR, and RL.
5. **What is hashing?** A technique that maps a key to a table index using a hash function.
6. **What is a collision?** When two different keys map to the same table index.
7. **What is linear probing?** On collision, check the next table position, continuing circularly until an empty slot or the key is found.
8. **Why can BST become O(n)?** Sorted or nearly sorted insertion can create a skewed tree.
9. **Why is AVL search O(log n)?** AVL maintains logarithmic tree height through rotations.
10. **Does hashing support sorted traversal?** Not naturally; a hash table is designed for key-based access, not ordered output.
