"""Runs repeatable search/insertion experiments on the same student dataset."""
import csv
from dataset import STUDENTS
from bst import BST
from avl import AVL
from hashing import LinearProbingHash

def average(values):
    return sum(values) / len(values) if values else 0

def main():
    bst, avl, htable = BST(), AVL(), LinearProbingHash(capacity=53)
    bst_insert_comparisons = avl_insert_count = hash_insert_collisions = 0

    # Same input order and records are supplied to all three implementations.
    for student in STUDENTS:
        # Count comparisons needed to locate the insertion position in BST/AVL
        _, c = bst.search(student["reg_no"])
        bst_insert_comparisons += c
        _, c = avl.search(student["reg_no"])
        avl_insert_count += c
        bst.insert(student)
        avl.insert(student)
        hash_insert_collisions += htable.insert(student)

    successful_keys = [STUDENTS[i]["reg_no"] for i in (0, 9, 19, 29, 39)]
    unsuccessful_keys = [605027499, 605027450, 605027500, 605027399, 605027488]

    results = []
    for label, keys in (("Successful", successful_keys), ("Unsuccessful", unsuccessful_keys)):
        for key in keys:
            for name, structure in (("BST", bst), ("AVL", avl), ("Hashing", htable)):
                record, comparisons = structure.search(key)
                results.append({
                    "search_type": label, "key": key, "structure": name,
                    "found": record is not None, "comparisons": comparisons
                })

    print("=" * 72)
    print("STUDENT RECORD SEARCH SYSTEM — EXPERIMENT OUTPUT")
    print(f"Dataset size: {len(STUDENTS)} records")
    print(f"BST height (levels): {bst.height()}")
    print(f"AVL height (levels): {avl.height()}")
    print(f"Hash table capacity: {htable.capacity}")
    print(f"Total collisions during hash insertion: {htable.collision_count()}")
    print(f"BST insertion-position search comparisons (aggregate): {bst_insert_comparisons}")
    print(f"AVL insertion-position search comparisons (aggregate): {avl_insert_count}")
    print(f"Hash insertion collisions (aggregate): {hash_insert_collisions}")
    print("-" * 72)
    print(f"{'Type':<15}{'Key':<15}{'Structure':<12}{'Found':<10}{'Comparisons'}")
    for r in results:
        print(f"{r['search_type']:<15}{r['key']:<15}{r['structure']:<12}{str(r['found']):<10}{r['comparisons']}")
    for name in ("BST", "AVL", "Hashing"):
        for label in ("Successful", "Unsuccessful"):
            vals = [r["comparisons"] for r in results if r["structure"] == name and r["search_type"] == label]
            print(f"Average {label.lower()} search comparisons — {name}: {average(vals):.2f}")

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader(); writer.writerows(results)
    print("\nDetailed search observations saved to results.csv")
    print("\nInorder traversal (first five records) — BST:")
    for r in bst.inorder()[:5]:
        print(r["reg_no"], r["name"])

if __name__ == "__main__":
    main()
