f :: [Int] -> [Int]
f lst = f' 1 lst

f' i lst | length lst == 0 = []
    | even i = (head lst) : f' (i+1) (tail lst)
    | otherwise = f' (i+1) (tail lst)

-- This part deals with the Input and Output and can be used as it is. Do not modify it.
main = do
   inputdata <- getContents
   mapM_ (putStrLn. show). f. map read. lines $ inputdata
