def main(list1,n,k):
    """
    A list of several elements is given. Return the value from n index to k index.
    Args:
        list1(list): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        list: return answer.
    """
    return list1[n:k]
list1=[1,2,3,4,5]
n=int(input())
k=int(input())
print(main(list1,n,k))