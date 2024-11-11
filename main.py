            ###### Questions  1 ######
# for i in  range(1,6):
#     print(i, end=" ")

# output 1 2 3 4 5 


            ###### Questions  2 ######


# for i in range(1,6):
#     print(i ** 2 , end=" ")

#  1 4 9 16 25

            ###### Questions  3 ######


# for i in range(1,11):
#     if i % 2 ==0:
#         print(i, end=" ")

# output 2 4 6 8 10

            ###### Questions  4 ######



# total=0
# for i in range(1,110):
#     total+=i
# print(f"Sum is {total}")

                    ###### Questions  5 ######



# word = 'python'
# for i in range(len(word)-1, -1, -1) :
#     print(word[i], end=" ")


                    ###### Questions  6 ######



# vowels= "aeiou"
# word="python django arham innsan"
# count= 0
# for char in word:
#     if char in vowels:
#         count += 1
# print(f"total vowels in {word} is {count}")


                    ###### Questions  7                                  #######
                 #######   print fabonacci sequence up to 10 term         #######



# a=0

# b=1

# print(a,b ,end=" ")

# for _ in range(10):
#     next_term=a+b
#     print(next_term, end=" ")
#     a,b = b,next_term



                    ###### Questions  8                                  #######


# n= 10
# factorial= 1

# for i in range(1, n+1):
#     factorial *=i

# print(f"factorial of {n} is {factorial}")


                    ###### Questions  9                            #######




# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

# # Example usage:
# print(find_missing_number([3, 7, 1, 2, 8, 4, 5]))  # Output: 6


# def longest_word(sentence):
#     words = sentence.split()
#     longest = max(words, key=len)
#     return longest

# # Example usage:
# print(longest_word("The quick brown fox jumps over the lazy dog"))

  # Output: "jumps"



# num = 7
# is_prime = True  # Start with the assumption that num is prime

# # Check divisibility from 2 up to the square root of num
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         is_prime = False  # num is not prime if divisible by i
#         break

# # Determine if num is prime
# if is_prime and num > 1:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
