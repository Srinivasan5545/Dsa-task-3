"""Interactive demonstration of the Student Record Search System."""
from dataset import STUDENTS
from bst import BST
from avl import AVL
from hashing import LinearProbingHash

def show_result(label, result):
    record, comparisons = result
    if record:
        print(f"{label}: FOUND | {record['name']} | {record['department']} | Year {record['year']} | comparisons={comparisons}")
    else:
        print(f"{label}: NOT FOUND | comparisons={comparisons}")

def main():
    bst, avl, table = BST(), AVL(), LinearProbingHash(53)
    for record in STUDENTS:
        bst.insert(record); avl.insert(record); table.insert(record)

    print("STUDENT RECORD SEARCH SYSTEM")
    print("Loaded", len(STUDENTS), "fictional sample records.")
    while True:
        print("\\n1. Search  2. Insert  3. Display BST inorder  4. Display AVL inorder  5. Show heights/collisions  0. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            try: key = int(input("Enter register number: "))
            except ValueError:
                print("Register number must be an integer."); continue
            show_result("BST", bst.search(key))
            show_result("AVL", avl.search(key))
            show_result("Hashing", table.search(key))
        elif choice == "2":
            try:
                key = int(input("Register number: "))
                name = input("Student name: ").strip()
                dept = input("Department: ").strip()
                year = int(input("Year (1-4): "))
                if not name or not dept or year not in (1, 2, 3, 4): raise ValueError
            except ValueError:
                print("Invalid input. Please enter valid details."); continue
            record = {"reg_no": key, "name": name, "department": dept, "year": year}
            bst.insert(record); avl.insert(record); table.insert(record)
            print("Record inserted/updated in all three structures.")
        elif choice == "3":
            for r in bst.inorder(): print(r)
        elif choice == "4":
            for r in avl.inorder(): print(r)
        elif choice == "5":
            print("BST height (levels):", bst.height())
            print("AVL height (levels):", avl.height())
            print("Hash collisions:", table.collision_count())
        elif choice == "0":
            print("Exiting."); break
        else:
            print("Choose a valid option.")

if __name__ == "__main__":
    main()
