# Tree ADT — 嵌套列表表示法: [label, branch1, branch2, ...]

# ============================================================
# 基础构造函数与访问器
# ============================================================

def is_tree(tree):
    """判断一个对象是否为合法的树结构."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """叶子节点: 没有分支的节点."""
    return not branches(tree)

def tree(label, branches=[]):
    """构造一棵树: tree(根标签, [子树列表])."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    """返回根节点标签."""
    return tree[0]

def branches(tree):
    """返回子树列表."""
    return tree[1:]


# ============================================================
# 示例树
# ============================================================
#
#       3
#      / \
#     1   2
#        / \
#       1   1
#
# t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
# t 的内部表示: [3, [1], [2, [1], [1]]]


# ============================================================
# 树的构造与遍历
# ============================================================

def fib_tree(n):
    """构造斐波那契树: 树的根标签为 fib(n), 左右子树分别为 fib(n-2) 和 fib(n-1) 的树."""
    if n <= 1:
        return tree(n)
    left, right = fib_tree(n - 2), fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])

def print_tree(t, indent=0):
    """缩进形式打印树结构."""
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def print_sums(t, so_far=0):
    """打印从根到每个叶子的路径和 (DFS)."""
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


# ============================================================
# 树上的递归操作
# ============================================================

def count_leaves(t):
    """统计叶子节点数量."""
    if is_leaf(t):
        return 1
    return sum(count_leaves(b) for b in branches(t))

def leaves(t):
    """返回所有叶子节点的标签列表."""
    if is_leaf(t):
        return [label(t)]
    return sum([leaves(b) for b in branches(t)], [])

def increment_leaves(t):
    """所有叶子标签 +1, 非叶子节点保持不变, 返回新树."""
    if is_leaf(t):
        return tree(label(t) + 1)
    bs = [increment_leaves(b) for b in branches(t)]
    return tree(label(t), bs)

def count_paths(t, total):
    """统计从根出发, 路径和等于 total 的路径数量 (终点不限叶子)."""
    paths_in_branches = sum(count_paths(b, total - label(t)) for b in branches(t))
    if label(t) == total:
        return paths_in_branches + 1
    return paths_in_branches
