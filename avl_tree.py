class AVLNode:
    def __init__(self, key, height=1):
        self.key = key
        self.height = height
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    # Получение высоты узла
    def get_height(self, node):
        return node.height if node else 0

    # Расчет баланса узла
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Поворот вправо
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Поворот влево
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Вставка узла
    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node  # Дубликаты не допускаются

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # Левый Левый случай
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Правый Правый случай
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Левый Правый случай
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Правый Левый случай
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # Обход дерева для тестов
    def in_order_traversal(self, node):
        if node:
            return self.in_order_traversal(node.left) + [node.key] + self.in_order_traversal(node.right)
        return []

    def display_tree(self):
        return self.in_order_traversal(self.root)
