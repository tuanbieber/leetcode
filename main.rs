
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	println!("{:?}", question::Solution::solve_sudoku());
}

