use rayon::prelude::*;

fn main() {
    // یک آرایه بزرگ از 1 تا 100
    let numbers: Vec<i32> = (1..=100).collect();

    // جمع موازی با rayon
    let sum: i32 = numbers.par_iter().sum();

    println!("مجموع اعداد 1 تا 100 = {}", sum);
}
