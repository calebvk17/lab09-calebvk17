# Lab 09 - Problem-Solving Practice 1

This lab is a set of **LeetCode / ICPC-style problems**. The goal isn't just a passing
test - it's practising the whole loop from *problem* to *plan* to *working code*, using
the problem-solving techniques from Unit 01 and the analysis ideas from Unit 04.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect.

## Getting Started

Accept the GitHub Classroom assignment invitation in Canvas (the link is in the lab
assignment on Canvas), which will clone your own copy of the repository. In the folder
where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab09-your-username
```

## How to approach each problem

Before writing (or generating) any code, spend a couple of minutes on the **outline**:

1. **Restate** the problem in your own words.
2. **Try a small example by hand** - what's the answer for a tiny input, and how did
   you get it?
3. **Sketch the approach** - what steps turn the input into the output? Is there an
   obvious brute-force way, and a faster way?

Each function in `lab09.py` has an `# Outline` comment - jot your plan there first. Once
you have a plan, *then* turn it into code (you may use an AI assistant to help - see
**Using AI** below).

## Problems

Edit **`lab09.py`**. Don't rename the functions - the tests use these names.

### Part 1 - `two_sum(nums, target)`

Return the two **indices** `[i, j]` (with `i < j`) of the numbers in `nums` that add up
to `target`. Assume exactly one pair works.

```python
two_sum([2, 7, 11, 15], 9)   # returns [0, 1]   (2 + 7)
two_sum([3, 2, 4], 6)        # returns [1, 2]   (2 + 4)
```

### Part 2 - `max_profit(prices)`

`prices[i]` is a stock's price on day `i`. Return the most profit you can make by buying
on one day and selling on a **later** day. If you can't make any profit, return `0`.

```python
max_profit([7, 1, 5, 3, 6, 4])   # returns 5   (buy at 1, sell at 6)
max_profit([7, 6, 4, 3, 1])      # returns 0   (prices only fall)
```

### Part 3 - `max_subarray(nums)`

Return the largest sum of any **contiguous** (in-a-row) block of numbers in `nums`. The
list has at least one number.

```python
max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])   # returns 6   (4 + -1 + 2 + 1)
max_subarray([5, 4, -1, 7, 8])                  # returns 23  (the whole list)
```

### Part 4 - `is_balanced(s)`  *(stretch - optional)*

Return `True` if every bracket in `s` is closed correctly and in the right order. The
brackets are `(` `)` `[` `]` `{` `}`.

```python
is_balanced("()[]{}")   # returns True
is_balanced("{[]}")     # returns True
is_balanced("([)]")     # returns False   (closed in the wrong order)
```

Hint: a **list used as a stack** (`append` to push, `pop` to remove the last item) is a
natural fit here.

This part is optional - the three problems above are the core of the lab.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

Read the output closely - a failing test shows the input, what it expected, and what
your code returned. Fix, save, and run `pytest` again.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Once your tests pass (or the session is ending), commit and push:

```
git add --all
git commit -m "Lab 09 completed"
git push origin main
```

You can confirm the autograder ran correctly by opening the **Actions** tab on your
repository page in GitHub. It can take a minute or two.

## Using AI

Starting this half of the term, you **may use an AI assistant to help you write the
code** for the lab. Build one habit first, though: **work out the problem-solving
outline yourself before you involve the AI.** For each problem, restate it, try a small
example by hand, and sketch your approach - *then* lean on the AI to help turn that plan
into Python. Let the AI do the implementing, not the thinking.

Use a free model, and be ready to **explain and modify** any code you submit - the lab
instructor may ask you to walk through it or change how it works.
