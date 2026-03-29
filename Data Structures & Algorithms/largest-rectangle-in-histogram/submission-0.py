class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Idea is that we want to delay the popping of elements
        from the stack until we see that there is a taller element
        For example, it the heights were [2,1,0,5,6] we put
        2 on the stack first and then 1 and then 0 and then once
        we hit 5, we can pop the 2 and calculate the biggest
        rectangle. we would also pop off 1 and 0. Essentially,
        we are trying to extend each height as far left and 
        as far right before we pop. The invariant is that if there
        is a bigger rectangle after, we can't "extend" anymore and
        so that's why we pop.

        '''
        N = len(heights)
        stack = []
        best = 0
        # trick is that our starting index in our stack should
        # be whatever was bigger to the left. Since we are only
        # processing when prev elements had a bigger height,
        # then subsequent elements that are smaller should
        # also go to this bigger element ie 7, 3, 1 -> 1 should
        # extend to the 7, not just the 3
        for index, height in enumerate(heights):
            start = index
            while len(stack) > 0 and stack[-1][1] > height:
                left_index, left_height = stack.pop()
                best = max(best, left_height * (index - left_index))
                start = left_index
            stack.append((start, height))
        print(stack)
        # we are left with a stack that is going to be
        # strictly increasing heights. We can extend each
        # as far right as possible
        for index, height in stack:
            best = max(best, height * (N - index))

        return best

