class Solution(object):
    def postorder(self, root):
        result = []
        if root != None:
            res = []
            for child in root.children:
                res += self.postorder(child)
            result += res
            result.append(root.val)
        return result

