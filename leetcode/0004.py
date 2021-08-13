
def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
    second_index = 0
    first_index = 0
    second_max = len(nums2)
    first_max = len(nums1)
    total_list = []
    total_len = first_max+second_max
    median_index = (total_len)/2
    if total_len % 2 ==0:
        double = True
        answer = [int(median_index), int(median_index-1)]
    else:
        double = False
        answer=[int(median_index-0.5)]
    if first_max ==0:
        return get_answer(nums2,double,answer)
    if second_max ==0:
        return get_answer(nums1,double,answer)
    for number, value in enumerate (nums1):
        while value > nums2 [second_index]:
            total_list.append(nums2[second_index])
            second_index+=1
            if second_index == second_max:
                total_list.extend(nums1[number:])
                return get_answer(total_list,double,answer)
        total_list.append (value)
        first_index+=1
        if first_index == first_max:
            total_list.extend(nums2[second_index:])
            return get_answer(total_list,double,answer)

def get_answer(total_list, double,answer ):
    if double:
        return (total_list[answer[0]] +total_list[answer[1]])/2
    else:
        return (total_list[answer[0]])


findMedianSortedArrays([],[1])