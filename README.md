# Student Record Search System — Algorithm Battle

**Course:** Data Structures and Algorithms (Continuous Learning Assessment – 2)  
**Institution:** SRM Institute of Science and Technology, Tiruchirappalli  
**Language:** Python 3

## Application selected
A Student Record Search System stores student details and retrieves a record using a unique register number. The same records are stored in a Binary Search Tree (BST), an AVL tree, and a hash table using linear probing.

## Files
- `main.py` — interactive menu for searching, inserting, and displaying traversals.
- `bst.py` — ordinary Binary Search Tree.
- `avl.py` — self-balancing AVL tree with LL, RR, LR, and RL rotations.
- `hashing.py` — hash table with linear probing.
- `dataset.py` — 40 fictional sample student records.
- `experiment.py` — runs the mini experiment and writes `results.csv`.
- `results.csv` — generated search observations (created after running experiment).

## Run
Open a terminal in this folder and run:

```bash
python main.py
```

To run the experiment:

```bash
python experiment.py
```

No third-party Python packages are required.

## Experiment design
All three data structures receive the same 40 records in the same insertion order. Five successful and five unsuccessful search keys are tested in each structure. The program counts key comparisons for each search, reports BST and AVL height in levels, and counts hash-table collisions during insertion. The detailed observations are exported to `results.csv`.

**Important:** The dataset is synthetic and the output is produced by executing the submitted code. Run the experiment on your own system and use its output in your final submission. Do not present example or unexecuted numbers as measured results.

## Complexity summary
| Structure | Search (typical) | Search (worst case) | Insertion (typical) |
|---|---:|---:|---:|
| BST | O(log n) if reasonably balanced | O(n) | O(log n) if reasonably balanced |
| AVL | O(log n) | O(log n) | O(log n) |
| Hashing | O(1) expected at a suitable load factor | O(n) | O(1) expected |

## GitHub submission
1. Create a new GitHub repository.
2. Upload the complete contents of this folder.
3. Add a short description and confirm that `README.md` explains how to run the program.
4. Copy the repository URL and submit it through Google Classroom.
