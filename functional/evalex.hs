import Control.Applicative
import Control.Monad
import System.IO


factorial :: Int -> Int
factorial x | x == 1 = 1 | otherwise = x * factorial (x-1)


ex :: Int -> Double -> Double
ex 0 x = 1
ex n x = ( (x ^ n) / (fromIntegral (factorial n)) ) + (ex (n-1) x)


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \a0  -> do
        x_temp <- getLine
        let x = read x_temp :: Double
        print (ex 9 x)

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

