def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[:n-1:-1]
list1=[1,2,3,4,5]
n=int(input())
print(main(list1,n,))