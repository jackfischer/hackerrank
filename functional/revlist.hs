rev :: [a] -> [a]

rev [] = []
rev (x:[]) = [x]

--rev (x:xs) =  (rev xs) ++ [x]
rev l = last l : rev (init l)