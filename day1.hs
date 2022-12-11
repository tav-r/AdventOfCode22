import System.IO

update :: [Ord] -> String -> [Ord]
update ls [] = [0] ++ ls
update l:ls s = l + read s ++ ls

main = do
    l <- getLine
    
