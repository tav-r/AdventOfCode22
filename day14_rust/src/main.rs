use std::io::stdin;

fn string_to_path(line: String) -> Vec<(u32, u32)> {
    let starts = line.split(" -> ").into_iter().map(|indices| {
        let indices = indices.split(',').fold(vec![], |mut acc, i| {
            acc.push(i.parse::<u32>().unwrap());
            acc
        });

        (indices[0], indices[1])
    });

    starts
        .clone()
        .zip(starts.skip(1))
        .inspect(|((x1, y1), (x2, y2))| println!("from: {}:{}, to: {}:{}", x1, y1, x2, y2))
        .flat_map(|((x1, y1), (x2, y2))| {
            let (fromx, tox) = if x1 <= x2 { (x1, x2) } else { (x2, x1) };
            let (fromy, toy) = if y1 <= y2 { (y1, y2) } else { (y2, y1) };

            (fromx..=tox)
                .map(move |x| (x, y1))
                .chain((fromy..=toy).map(move |y| (x2, y)))
        })
        .collect()
}

fn find_sand_position(
    from: (u32, u32),
    sand: &[(u32, u32)],
    paths: &[(u32, u32)],
) -> Option<(u32, u32)> {
    let (mut x, mut y) = from;

    loop {
        if paths.iter().all(|(_, y_path)| *y_path <= y) {
            break None;
        } else if !paths.contains(&(x, y + 1)) && !sand.contains(&(x, y + 1)) {
            y += 1
        } else if !paths.contains(&(x - 1, y + 1)) && !sand.contains(&(x - 1, y + 1)) {
            (x, y) = (x - 1, y + 1)
        } else if !paths.contains(&(x + 1, y + 1)) && !sand.contains(&(x + 1, y + 1)) {
            (x, y) = (x + 1, y + 1)
        } else {
            break Some((x, y));
        }
    }
}

fn find_sand_position2(
    from: (u32, u32),
    sand: &[(u32, u32)],
    paths: &[(u32, u32)],
) -> Option<(u32, u32)> {
    let (mut x, mut y) = from;

    let res = loop {
        if paths.iter().all(|(_, y_path)| *y_path < y) {
            break (x, y);
        } else if !paths.contains(&(x, y + 1)) && !sand.contains(&(x, y + 1)) {
            y += 1
        } else if !paths.contains(&(x - 1, y + 1)) && !sand.contains(&(x - 1, y + 1)) {
            (x, y) = (x - 1, y + 1)
        } else if !paths.contains(&(x + 1, y + 1)) && !sand.contains(&(x + 1, y + 1)) {
            (x, y) = (x + 1, y + 1)
        } else {
            break (x, y);
        }
    };

    if res.1 == 0 {
        None
    } else {
        Some(res)
    }
}

fn main() {
    let paths: Vec<(u32, u32)> = stdin()
        .lines()
        .map(|l| l.unwrap())
        .flat_map(string_to_path)
        .collect();

    let sand1 = (0..).try_fold(vec![], |mut sand, i| {
        find_sand_position((500, 0), &sand, &paths)
            .map(|position| {
                sand.push(position);
                sand
            })
            .ok_or(i)
    });

    dbg!(sand1);

    let sand2 = (1..).try_fold(vec![], |mut sand, i| {
        find_sand_position2((500, 0), &sand, &paths)
            .map(|position| {
                sand.push(position);
                sand
            })
            .ok_or(i)
    });

    dbg!(sand2);
}
