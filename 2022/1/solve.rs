use std::fs::File;
use std::io::{BufReader, Read};

fn main() {
    let file = File::open("input.txt").unwrap();
    let mut reader = BufReader::new(file);
    let mut content = String::new();
    reader.read_to_string(&mut content).unwrap();

    let mut sums: Vec<i32> = content.split("\n\n")
                                    .map(|chunk| chunk.split("\n")
                                                    .map(|x| x.parse::<i32>().unwrap())
                                                    .sum())
                                    .collect();

    println!("part1: {}", sums.iter().max().unwrap());

    sums.sort();
    println!("part2: {}", sums.iter()
                              .rev()
                              .take(3)
                              .map(|x| *x)
                              .sum::<i32>()
                            )
}
