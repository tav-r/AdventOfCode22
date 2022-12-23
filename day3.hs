import Data.Char (isLower, ord)

priority :: Char -> Int
priority c =
  if isLower c
    then 1 + ord c - ord 'a'
    else 27 + ord c - ord 'A'

rucksackVal :: [String] -> Char
rucksackVal ss = head [c | c <- head ss, all (c `elem`) (drop 1 ss)]

partition :: Int -> [a] -> [[a]]
partition n [] = []
partition n as = take n as : partition n (drop n as)

main = do
  puzzleInput <- lines <$> getContents
  print $ sum $ priority . rucksackVal . (\s -> partition (length s `div` 2) s) <$> puzzleInput
  print $ sum $ priority . rucksackVal <$> partition 3 puzzleInput