import Data.List

update :: [Int] -> String -> [Int]
update [] s = [read s :: Int]
update xs [] = 0 : xs
update (x : xs) s = (x + read s :: Int) : xs

main = do
  res <- reverse . sort . foldl update [] . lines <$> getContents
  print $ head res
  print $ sum $ take 3 res
