

values = [a^b | a <- [2..100], b <- [2..100]]

-- -----------------------
-- | Solves https://projecteuler.net/problem=29
--

filterNonUnique :: Eq a => [a] -> [a]
filterNonUnique [] = []
filterNonUnique [x] = [x]
filterNonUnique (x:xs) = if elem x xs 
						 then [x] ++ (filterNonUnique xs)
						 else [x] ++ (filterNonUnique xs)


main = print (length(filterNonUnique values))