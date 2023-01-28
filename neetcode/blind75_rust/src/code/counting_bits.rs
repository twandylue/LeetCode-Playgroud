pub struct Solution {}

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut counter: Vec<i32> = Vec::from([0]);
        for i in 1..=n {
            counter.push(counter[i as usize >> 1] + i % 2);
        }

        counter
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let n = 2;
        let expected = vec![0, 1, 1];
        let actual = Solution::count_bits(n);
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let n = 5;
        let expected = vec![0, 1, 1, 2, 1, 2];
        let actual = Solution::count_bits(n);
        assert_eq!(expected, actual);
    }
}
