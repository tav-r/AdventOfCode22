use std::{cmp::Ordering, io::stdin, ops::Deref};

#[derive(Clone, Debug, PartialEq)]
enum ListMember {
    Number(u32),
    List(Vec<ListMember>),
}

impl PartialOrd for ListMember {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        match (&self, other) {
            (ListMember::Number(n), ListMember::Number(m)) => n.partial_cmp(m),
            (ListMember::List(j), ListMember::List(l)) => ordered(j, l),
            (ListMember::Number(n), other_member) => {
                let dummy_list = ListMember::List(vec![ListMember::Number(*n)]);

                dummy_list.partial_cmp(other_member)
            }
            (this_member, ListMember::Number(m)) => {
                let dummy_list = ListMember::List(vec![ListMember::Number(*m)]);

                this_member.deref().partial_cmp(&dummy_list)
            }
        }
    }
}

fn parse_number(list_str: &'_ str) -> (Option<ListMember>, &'_ str) {
    let res_str = list_str
        .chars()
        .take_while(|c| ('0'..='9').contains(c))
        .collect::<String>();

    match res_str.parse::<u32>().map(ListMember::Number) {
        Ok(res) => (Some(res), &list_str[res_str.len()..]),
        Err(_) => (None, list_str),
    }
}

fn parse_list(list_str: &'_ str) -> (Option<ListMember>, &'_ str) {
    let mut rest = list_str;
    let mut res = vec![];

    loop {
        if let Some(next_char) = rest.chars().next() {
            let (maybe_member, new_rest) = match next_char {
                '[' => parse_list(&rest[1..]),
                '0'..='9' => parse_number(rest),
                ',' | ' ' => (None, &rest[1..]),
                ']' => break (Some(ListMember::List(res)), &rest[1..]),
                _ => panic!("unexpected token"),
            };

            if let Some(member) = maybe_member {
                res.push(member);
            }

            rest = new_rest;
        } else {
            break (Some(ListMember::List(res)), rest);
        }
    }
}

fn ordered(a: &[ListMember], b: &[ListMember]) -> Option<Ordering> {
    if a.is_empty() {
        a.len().partial_cmp(&b.len())
    } else if b.is_empty() {
        Some(Ordering::Greater)
    } else {
        match a[0].partial_cmp(&b[0]) {
            Some(Ordering::Equal) => ordered(&a[1..], &b[1..]),
            other => other,
        }
    }
}

fn main() {
    let mut lists: Vec<ListMember> = stdin()
        .lines()
        .filter_map(|maybe_l| {
            maybe_l.ok().and_then(|l| {
                if !l.is_empty() {
                    Some(parse_list(&l).0.expect("could not parse line"))
                } else {
                    None
                }
            })
        })
        .collect();

    let part1 = lists
        // iterate in tuple-windows of size 2
        .iter()
        .step_by(2)
        .zip(lists.iter().skip(1).step_by(2))
        // get indices (starting by 1) for each pair for which the first element is smaller than the second
        // and calculate sum over these indices
        .map(|(a, b)| a < b)
        .enumerate()
        .filter(|(_, val)| *val)
        .map(|(index, _)| index + 1)
        .sum::<usize>();

    println!("index sum is {}", part1);

    let markers = ["[[2]]", "[[6]]"]
        .iter()
        .map(|marker_str| parse_list(marker_str).0.unwrap());

    // add markers to litss
    markers.clone().for_each(|m| lists.push(m));

    lists.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // get indices of markers
    let part2: usize = markers
        .map(|marker| lists.iter().position(|a| *a == marker).unwrap() + 1)
        .product();

    println!("marker index product: {}", part2)
}
