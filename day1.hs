import Data.List

update :: [Int] -> String -> [Int]
update xs [] = [0] ++ xs
update (x:xs) s = [x + read s :: Int] ++ xs

main = do
    res <- reverse . sort . foldl update [0] . lines <$> getContents
    print $ res !! 0
    print $ sum $ take 3 res
