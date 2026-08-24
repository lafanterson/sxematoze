import Data.List (group)

maxConsecutiveEqual :: (Eq a) => [a] -> Int
maxConsecutiveEqual xs = maximum (map length (group xs))

main :: IO ()
main = do
    let sequence = [1, 1, 2, 2, 2, 3, 3, 2, 2]
    print (maxConsecutiveEqual sequence)
