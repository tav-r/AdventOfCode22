use std::io;

fn main() {
    let mut calories: Vec<i32> = io::stdin()
        .lines()
        .map(|maybe_line| maybe_line.unwrap().trim().to_string())
        .fold(vec![0], |mut v, l| {
            if !l.is_empty() {
                v[0] += l.parse::<i32>().unwrap();
                v
            } else {
                v.push(0);
                v.rotate_right(1);
                v
            }
        })
        .into_iter()
        .collect();

    calories.sort();
    calories.reverse();

    let max_calories = calories.first().unwrap();
    let sum_top_three: i32 = calories.iter().take(3).sum();

    println!(
        "maximum calories carried by a single elf: {}, top three elves carry {}",
        max_calories, sum_top_three
    );
}
