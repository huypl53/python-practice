class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split('/')
        stack = list()
        for item in items:
            if not item or item == '.': continue
            if item == '..': 
                if stack: stack.pop()
            else: stack.append(item)

        return '/'+'/'.join(stack)
