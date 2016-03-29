

{-

-- TODO: Cache data to improve time complexity


import Data.Map (Map)
import qualified Data.Map as Map

data CoordinateCache = Map (Integer, Integer) Integer 

cache :: CoordinateCache 
cache = Map.fromList []


updateCache :: (Map a  a , Eq b, Num b) => a -> b -> b -> b -> a
updateCache cache keyPt1 keyPt2 value = do 
	case Map.lookup cache (keyPt1,keyPt2) of 
		Nothing -> let cache' = Map.insert (keyPt1, keyPt2) value cache' in cache'
		Just value -> cache 


updateIfExists :: (Ord a, Eq b, Num b) => b -> a -> a -> a -> b
updateIfExists cache xCoord yCoord edge 
	| elem (xCoord, yCoord) cache

-}


-- -------------------
-- | Each coordinate allows travel in two directions, except for edge coordinates.
-- | Thus, we recursively travel in both directions until an edge coordinate is found
-- | which serves as our base condition.
--

traverseUntilEdge :: (Eq a, Num a) => a -> a -> a -> a
traverseUntilEdge xCoord yCoord edge 
	| xCoord == edge = 1
	| yCoord == edge = 1
	| otherwise = (traverseUntilEdge (xCoord+1) yCoord edge) + (traverseUntilEdge xCoord (yCoord+1) edge)
	

main = print (traverseUntilEdge 0 0 20)

