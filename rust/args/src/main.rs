extern crate clap;

use clap::{App, Arg};

fn main() {
    let matches = App::new("args")
        .about("Example args project.")
        .arg(
            Arg::with_name("arg1")
                .short("a")
                .long("arg1")
                .required(true)
                .takes_value(true)
                .value_name("ARG1")
                .help("The first argument.")
        ).get_matches();
    println!("{}", matches.value_of("arg1").unwrap());
}
