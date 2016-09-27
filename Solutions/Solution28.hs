

-- -----------------------
-- | Solves https://projecteuler.net/problem=28
--

numberSpiralSum :: Int -> Int 
numberSpiralSum dim
    | (dim < 1) || (dim `mod` 2 == 0) = error invalidInputMessage
    | dim == 1 = 1
    | otherwise =  prevSum + numberSpiralSum (dim-2)
    where prevSum = sum [(dim*dim) - i*(dim-1) | i <- [0..3]]
          invalidInputMessage = "Invalid! Input must be positive, odd number"


main = print (numberSpiralSum 1001)