use std::io::stdin;
fn main() {
    let cycles = stdin().lines().fold(vec![1], |mut cycles, maybe_line| {
        maybe_line
            .map(|line| {
                let counter = cycles.last().copied().unwrap();

                match line.trim() {
                    // addx does not change the counter for one cycle and adds
                    // its operand to the counter the next cycle
                    instr if line.starts_with("addx") => {
                        let (_, operand_str) = instr.split_at(5);
                        let operand = operand_str.parse::<i32>().unwrap();

                        cycles.push(counter);
                        cycles.push(counter + operand);
                    }
                    // noop does not change anything for one cycle
                    _ if line.starts_with("noop") => {
                        cycles.push(counter);
                    }
                    // skip empty lines
                    _ if line.is_empty() => (),
                    _ => panic!("unexpected input"),
                };
            })
            .ok();

        cycles
    });

    let res1: i32 = (20..=220)
        .step_by(40)
        .map(|i| cycles[i - 1] * std::convert::TryInto::<i32>::try_into(i).unwrap())
        .sum();

    dbg!(res1);

    // part 2
    let res2 = cycles
        .iter()
        .enumerate()
        .map(|(pos, sprite)| {
            let pos_signed = (std::convert::TryInto::<i32>::try_into(pos).unwrap()) % 40;
            if (sprite - 1..=sprite + 1).contains(&pos_signed) {
                '#'
            } else {
                '.'
            }
        })
        .collect::<String>();

    (0..=220)
        .step_by(40)
        .into_iter()
        .for_each(|i| println!("{}", &res2[i..i + 40]));
}
