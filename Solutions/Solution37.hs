
-- Definitions --
-- | A truncation is defined as removing digits from an integer.
-----------------


--------------
-- | Returns all prime truncations.
--
primeTruncations :: [Integer] -> Integer -> [Integer]
primeTruncations vals index
  | length vals == bound = vals
  | otherwise = if bothTruncationsArePrime index
                then primeTruncations (index : vals) (updateIndex index)
                else primeTruncations vals (updateIndex index)
                where bound = 11 -- this is the theoretical limit


--------------
-- | Optimized index update, rather than just incrementing by one.
-- |
-- | If an even is encountered, this function provides the largest update possible.
--
updateIndex :: Integer -> Integer
updateIndex index
  | endIsTwo index = index + 1
  | containsEven index = (10 ^ (positionOfFirstEven index)) + index
  | otherwise = index + 2


--------------
-- | Returns true if either the first or last digit of the input
-- | is true. This is used as a helper of the updateIndex function.
--
endIsTwo :: Integer -> Bool
endIsTwo val = frontIsEven || endIsTwo
  where frontIsEven = (stringToInt $ [head $ show val]) == 2
        endIsTwo = (stringToInt $ [last $ show val]) == 2


--------------
-- | Returns true if the input contains an even value, other than two.
--
containsEven :: Integer -> Bool
containsEven val
  | val < 10 = isEvenValueOtherThanTwo val
  | otherwise = if isEvenValueOtherThanTwo (stringToInt $ [last str])
                then True
                else containsEven $ stringToInt $ init $ str
                where str = show val


isEvenValueOtherThanTwo :: Integer -> Bool
isEvenValueOtherThanTwo val = (val `mod` 2 == 0) && (val /= 0)


positionOfFirstEven :: Integer -> Integer
positionOfFirstEven val
  | not $ containsEven val = error "Does not contain even"
  | otherwise = positionOfFirstEvenHelper val strLength
  where strLength = (toInteger $ length $ show val) - 1


--------------
-- | This helper-function assumes that the input does contain an even digit.
-- |
-- | The function removes the first digit until an even number is found.
--
positionOfFirstEvenHelper :: Integer -> Integer -> Integer
positionOfFirstEvenHelper val pos = do
              if val < 10
              then 0
              else do
                if headVal `mod` 2 == 0
                then pos
                else positionOfFirstEvenHelper remainderOfListWithHeadRemoved (pos-1)
                where headVal = stringToInt $ [head $ show val]
                      remainderOfListWithHeadRemoved = (stringToInt $ tail $ show val)


--------------
-- | Returns the some of prime truncations. The number of truncations
-- | that are summed is specified by the bound input integer.
--
sumOfPrimeTruncations :: Integer
sumOfPrimeTruncations
  | otherwise = sum $ primeTruncations [] startingIndex
  where startingIndex = 10 -- truncations must be >= 10


--------------
-- | Returns true if both left and right trunctations are prime.
--
bothTruncationsArePrime :: Integer -> Bool
bothTruncationsArePrime val = leftTruncationsArePrime val && rightTruncationsArePrime val


--------------
-- | Returns true if, when each digit is removed from
-- | the left, the resulting integer remains prime.
--
leftTruncationsArePrime :: Integer -> Bool
leftTruncationsArePrime val
  | val < 10 = isPrime val
  | otherwise = isPrime val && (leftTruncationsArePrime $ stringToInt $ init $ show val)
    where singleDigitBound = 10


--------------
-- | Returns true if, when each digit is removed from
-- | the right, the resulting integer remains prime.
--
rightTruncationsArePrime :: Integer -> Bool
rightTruncationsArePrime val
  | val < singleDigitBound = isPrime val
  | otherwise = isPrime val && (rightTruncationsArePrime $ stringToInt $ tail $ show val)
    where singleDigitBound = 10


stringToInt :: [Char] -> Integer
stringToInt str = read str :: Integer


isPrime :: Integer -> Bool
isPrime val
  | (val == 0) || ((abs val) == 1) = False
  | otherwise = length divisors == 0
    where divisors = [n | n <- [2..divisorUpperBound], val `mod` n == 0]
          divisorUpperBound = floor $ sqrt $ fromIntegral val


-- main =
