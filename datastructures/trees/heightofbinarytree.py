
    def getHeight(self, root):
        #Write your code here
        def heightRecur(root: Node) -> int:
            if root is None:
                return 0
            l = heightRecur(root.left)
            r = heightRecur(root.right)
            return max((l,r)) + 1

        #print(heightRecur(root) - 1)
        return (heightRecur(root) - 1)
