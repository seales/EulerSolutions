
-- Values were explicit in the problem -------------------------------
upperBound = 1000000
exponentToValueMap = [2^n | n <- [0..floor(logBase 2 (fromIntegral upperBound))]]
----------------------------------------------------------------------


isPalindrome :: [Char] -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome str = ((head str) == (last str)) && isPalindrome endsRemoved
	where 	endsRemoved = [str !! i | i <- [1..(length str)-2]]


canSubtractExp :: Int -> Int -> Bool 
canSubtractExp index val = (exponentToValueMap !! index) <= val 


subtractExp :: Int -> Int -> Int 
subtractExp index val = val - (exponentToValueMap !! index)


convertDecimalToBinaryHelper :: Int -> Int -> [Char]
convertDecimalToBinaryHelper index val 
	| (index == 0) && (val == 0) = "0"
	| (index == 0) && (val == 1) = "1"
	|otherwise = if canSubtractExp index val 
			     then "1" ++ convertDecimalToBinaryHelper (index-1) (subtractExp index val)
			     else "0" ++ convertDecimalToBinaryHelper (index-1) val


convertDecimalToBinary :: Int -> [Char]
convertDecimalToBinary val = convertDecimalToBinaryHelper initialIndex val 
	where 	initialIndex = floor(logBase 2 (fromIntegral val))


sumOfPalindromesLessThanBound :: Int 
sumOfPalindromesLessThanBound = sum palindromes
	where 	palindromes = [i | i <- [0..upperBound], isPalindrome (show i), isPalindrome (convertDecimalToBinary i)]
			-- binaryConstraint = isPalindrome (convertDecimalToBinary i)
			-- decimalConstraint = isPalindrome (read i)


main = print (show sumOfPalindromesLessThanBound)

