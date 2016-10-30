f :: Int -> [Int] -> [Int]
f n arr = f' n n arr

--m is original total
f' :: Int -> Int -> [Int] -> [Int]

--all out of input
f' m n [] = []

--reset, do next number from input
f' m 0 (head:tail) = (f' m m tail)

--middle of iterations
f' m n (head:tail) = (head : (f' m (n-1) (head:tail) ))



-- This part handles the Input and Output and can be used as it is. Do not modify this part.
main :: IO ()
main = getContents >>=
       mapM_ print. (\(n:arr) -> f n arr). map read. words
