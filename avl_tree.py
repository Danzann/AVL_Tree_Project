class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Получить высоту узла
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Получить баланс узла
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Поворот вправо
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Выполняем поворот
        x.right = y
        y.left = T2

        # Обновляем высоты
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Возвращаем новый корень
        return x

    # Поворот влево
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Выполняем поворот
        y.left = x
        x.right = T2

        # Обновляем высоты
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Возвращаем новый корень
        return y

    # Вставка нового узла
    def insert(self, root, key):
        if not root:
            return AVLTreeNode(key)

        # Вставляем ключ в дерево
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Обновляем высоту текущего узла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Проверяем баланс и выполняем повороты, если необходимо
        balance = self.get_balance(root)

        # Левый левый случай
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Правый правый случай
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Левый правый случай
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Правый левый случай
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Вставка нового ключа в АВЛ-дерево
    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # Обход дерева in-order (по возрастанию)
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

    # Вывод дерева
    def display_tree(self):
        return self.inorder(self.root)

# Тестирование
def test_avl_tree():
    avl_tree = AVLTree()
    
    # Вставляем элементы
    avl_tree.insert_key(10)
    avl_tree.insert_key(20)
    avl_tree.insert_key(5)
    avl_tree.insert_key(6)
    avl_tree.insert_key(15)

    # Выводим элементы дерева в порядке возрастания
    print("Дерево после вставки: ", avl_tree.display_tree())

    # Добавляем еще элементы
    avl_tree.insert_key(3)
    avl_tree.insert_key(30)
    
    # Выводим обновленное дерево
    print("Дерево после вставки еще нескольких элементов: ", avl_tree.display_tree())

test_avl_tree()
