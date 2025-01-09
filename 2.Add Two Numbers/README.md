# Steps:

    1.	Initialize pointers and carry:
            -Use pointers to traverse the two linked lists and a variable carry to store the carry-over during addition.
    2.	Iterate through both linked lists:
        	-Add corresponding digits from the two lists along with the carry.
            -Compute the new digit (sum % 10) and update the carry (sum // 10).
            -Create a new node with the computed digit and link it to the result.
    3.	Handle remaining carry:
            -After finishing the lists, if carry is not zero, add a new node with the value of carry.
    4.	Return the result list.

- 9 jan 2025
