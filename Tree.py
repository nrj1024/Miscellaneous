class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class TreeUtils:
    @classmethod
    def insert(cls,root,data):
        if root==None:
            print("Inserted",data)
            return TreeNode(data)
        elif root.data==None:
            root.data=data
        elif root.data==data:
            print(data,"already exists!")
            return root
        elif data>root.data:
            root.right=cls.insert(root.right,data)
        else:
            root.left=cls.insert(root.left,data)
        return root
    @classmethod
    def inorder(cls,root):
        if root!=None:
            cls.inorder(root.left)
            print(root.data)
            cls.inorder(root.right)

tree1=TreeNode(3)
TreeUtils.insert(tree1,3)
TreeUtils.insert(tree1,5)
TreeUtils.insert(tree1,7)
TreeUtils.insert(tree1,1)
TreeUtils.insert(tree1,2)

TreeUtils.inorder(tree1)