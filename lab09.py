# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    
    # The goal is to find two numbers in the list that add up to the target
    # and return the positions of those two numbers.
    
    # Example: nums = [2, 7, 11, 15], target = 9
    # 2 + 7 = 9, so the answer would be [0, 1].

    # One way is to compare every number with the numbers after it.
    # This is the brute force approach because it checks every possible pair.
    # A faster way would be to use a dictionary to keep track of numbers
    # already seen and check if the number is there.
    
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def max_profit(prices):
    # Outline:
    
    # The goal is to find the biggest profit possible by buying a stock
    # and selling it on a later day.

    # Example: prices = [7, 1, 5, 3, 6, 4]
    # Buy at 1 and sell at 6, which gives a profit of 5.

    # A basic way is to check every possible buying and selling day.
    # A faster way is to go through the list once and keep track of
    # the lowest price so far and the biggest profit.
    # Update these values as you go through the list.
    # Return the biggest profit found, or 0 if there is no profit.

    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    
    if len(prices) == 0:
        return 0
    
    lowestPrice = prices[0]
    biggestProfit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - lowestPrice

        if profit > biggestProfit:
            biggestProfit = profit

        if prices[i] < lowestPrice:
            lowestPrice = prices[i]

    return biggestProfit

def max_subarray(nums):
    # Outline:

    # The goal is to find the biggest sum possible from numbers
    # that are beside each other in the list.

    # Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # The biggest sum is 6 from [4, -1, 2, 1].

    # A basic way is to check every possible group of numbers
    # and calculate their sums.
    # A faster way is to keep track of the current sum and the highest sum.
    # For each number, decide if you should add it to the current group
    # or start a new group with that number.
    # Update the highest sum whenever you find a bigger one.

    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    
    currentSum = nums[0]
    biggestSum = nums[0]

    for i in range(1, len(nums)):
        if currentSum + nums[i] > nums[i]:
            currentSum = currentSum + nums[i]
        else:
            currentSum = nums[i]

        if currentSum > biggestSum:
            biggestSum = currentSum

    return biggestSum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:

    # The goal is to check if all brackets in the string are opened
    # and closed properly and in the correct order.

    # Example: s = "{[]}"
    # The brackets are closed correctly and they are in the right order, so the answer is True.
    # An example like "([)]" would return False because they are
    # closed in the wrong order.

    # A basic way would be to check matching bracket pairs.
    # A better way is to use a list as a stack.
    # Go through each character and add opening brackets to the stack.
    # When a closing bracket appears, check if it matches the last
    # opening bracket. If it does not match, return False.
    # At the end, return True only if the stack is empty.

    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    
    stack = []

    for bracket in s:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            last = stack.pop()

            if bracket == ")" and last != "(":
                return False
            if bracket == "]" and last != "[":
                return False
            if bracket == "}" and last != "{":
                return False

    return len(stack) == 0

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # returns [0, 1]   (2 + 7)
    print(two_sum([3, 2, 4], 6))        # returns [1, 2]   (2 + 4)
    print(max_profit([7, 1, 5, 3, 6, 4]))   # returns 5   (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))      # returns 0   (prices only fall)
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]))                  # returns 23  (the whole list)
    print(is_balanced("()[]{}"))   # returns True
    print(is_balanced("{[]}"))     # returns True
    print(is_balanced("([)]"))     # returns False   (closed in the wrong order)

if __name__ == "__main__":
    main()
