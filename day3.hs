import Data.Char (isLower, ord)

priority :: Char -> Int
priority c =
  if isLower c
    then 1 + ord c - ord 'a'
    else 27 + ord c - ord 'A'

rucksackPrio :: [String] -> Int
rucksackPrio ss = priority $ head [c | c <- head ss, all (c `elem`) (drop 1 ss)]

partition :: Int -> [a] -> [[a]]
partition n [] = []
partition n as = take n as : partition n (drop n as)

main = do
  puzzleInput <- lines <$> getContents
  print $ sum $ rucksackPrio . (\s -> partition (length s `div` 2) s) <$> puzzleInput
  print $ sum $ rucksackPrio <$> partition 3 puzzleInput