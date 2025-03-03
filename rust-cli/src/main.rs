use clap::Parser;

#[derive(Parser, Debug)]
#[clap(author, version, about)]
struct Args {
    #[arg()]
    name: Option<String>,
}

fn main() {
    let args = Args::parse();
    let name = args.name.as_ref().map_or("world", |v| v);
    println!("Hello, {}!", name);
}
