use std::fs::File;
use std::io::{BufReader, Read};

fn main() {
    let file = File::open("input.txt").unwrap();

    let mut reader = BufReader::new(file);

    let mut content = String::new();
    reader.read_to_string(&mut content).unwrap();

    let chunks: Vec<&str> = content.split("\n\n").collect();

    let mut sums: Vec<i32> = Vec::new();
    for chunk in chunks {
        let mut sum = 0;
        for line in chunk.split("\n") {
            let num = line.parse::<i32>().unwrap();
            sum += num;
        }
        sums.push(sum);
    }

    println!("max: {}", sums.iter().max().unwrap());
}
