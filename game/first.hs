maxEvenSegment :: [Int] -> Int
maxEvenSegment = go 0 0
  where
    go currentMax currentLen [] = currentMax
    go currentMax currentLen (x:xs)
      | even x    = go currentMax (currentLen + 1) xs
      | otherwise = go (max currentMax currentLen) 0 xs

main :: IO ()
main = do
    let n = 10
    let sequence = [2, 4, 6, 1, 2, 4, 8, 10, 3, 2]
    print (maxEvenSegment sequence)
