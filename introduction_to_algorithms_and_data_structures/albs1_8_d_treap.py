class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def right_rotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def left_rotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, t, key, priority):
        if t is None:
            return Node(key, priority)

        if key == t.key:
            return t

        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.right_rotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.left_rotate(t)

        return t

    def delete(self, t, key):
        if t is None:
            return None

        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return (
                t.left
                if t.right is None
                else t.right
                if t.left is None
                else self.delete(
                    t, t.left.key if t.left.priority < t.right.priority else t.right.key
                )
            )

        return t

    def find(self, t, key):
        if t is None or t.key == key:
            return t
        if key < t.key:
            return self.find(t.left, key)
        return self.find(t.right, key)

    def inorder(self, t, result):
        if t is None:
            return
        self.inorder(t.left, result)
        result.append(t.key)
        self.inorder(t.right, result)

    def preorder(self, t, result):
        if t is None:
            return
        result.append(t.key)
        self.preorder(t.left, result)
        self.preorder(t.right, result)


def main():
    m = int(input())
    treap = Treap()

    for _ in range(m):
        command = input().split()

        if command[0] == "insert":
            treap.root = treap.insert(treap.root, int(command[1]), int(command[2]))
        elif command[0] == "find":
            print("yes" if treap.find(treap.root, int(command[1])) else "no")
        elif command[0] == "delete":
            treap.root = treap.delete(treap.root, int(command[1]))
        elif command[0] == "print":
            inorder_result = []
            treap.inorder(treap.root, inorder_result)
            print(" ".join(f" {k}" for k in inorder_result))

            preorder_result = []
            treap.preorder(treap.root, preorder_result)
            print(" ".join(f" {k}" for k in preorder_result))


if __name__ == "__main__":
    main()
